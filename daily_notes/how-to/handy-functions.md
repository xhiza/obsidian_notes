---
id: handy-functions
aliases: []
tags: []
---

List instances per region with status running and specified tags

```go
func listEC2Instances(region string, tagKey string, tagValue string) ([]\*ec2.Instance, error) {
sess, err := session.NewSession(&aws.Config{
Region: aws.String(region)},
)
if err != nil {
return nil, fmt.Errorf("failed to create session: %v", err)
}

    svc := ec2.New(sess)

    input := &ec2.DescribeInstancesInput{
    	Filters: []*ec2.Filter{
    		{
    			Name: aws.String("tag:" + tagKey),
    			Values: []*string{
    				aws.String(tagValue),
    			},
    		},
    		{
    			Name: aws.String("instance-state-name"),
    			Values: []*string{
    				aws.String("running"),
    			},
    		},
    	},
    }

    result, err := svc.DescribeInstances(input)
    if err != nil {
    	return nil, fmt.Errorf("failed to describe instances: %v", err)
    }

    var instances []*ec2.Instance
    for _, reservation := range result.Reservations {
    	instances = append(instances, reservation.Instances...)
    }

    return instances, nil

}
```

Send shell script to instance

```go

func senShellScript(region, instanceid string) (string, error) {

	session, err := session.NewSession(&aws.Config{
		Region: aws.String(region),
	})

	if err != nil {
		fmt.Println("Error creating new session:", err)
		return "", err
	}

	svc := ssm.New(session)

	shell_script := `
#!/bin/bash

cat <<EOL > /etc/systemd/system/unattended-upgrades.service
[Unit]
Description=Unattended Upgrades

[Service]
Type=oneshot
ExecStart=/usr/bin/unattended-upgrade -v
EOL


cat <<EOL > /etc/systemd/system/unattended-upgrades.timer
[Unit]
Description=Run Unattended Upgrades 15minutes after boot and every day.

[Timer]
OnCalendar=
OnBootSec=15min
OnUnitActiveSec=1d
AccuracySec=1h
RandomizedDelaySec=30min
Persistent=true

[Install]
WantedBy=timers.target
EOL

sudo systemctl daemon-reload
sudo systemctl enable unattended-upgrades.timer
sudo systemctl start unattended-upgrades.timer

# Uncomment the specified line in 50unattended-upgrades
sudo sed -i '/^.*"${distro_id}:${distro_codename}-updates";/s/^\/\///' /etc/apt/apt.conf.d/50unattended-upgrades

echo "Directories and files created successfully, systemd reloaded, and 50unattended-upgrades updated."
`
	sendCommandInput := &ssm.SendCommandInput{
		InstanceIds: []*string{
			aws.String(instanceid),
		},
		DocumentName: aws.String("AWS-RunShellScript"),
		Comment:      aws.String("unattended-upgrades"),
		Parameters: map[string][]*string{
			"commands": {
				aws.String(shell_script),
			},
		},
	}

	res, err := svc.SendCommand(sendCommandInput)
	if err != nil {
		fmt.Println(err)
		return "", err
	}

	time.Sleep(5 * time.Second)
	getCommandOutputInput := &ssm.GetCommandInvocationInput{
		CommandId:  res.Command.CommandId,
		InstanceId: &instanceid,
	}

	resultCommandOutput, err := svc.GetCommandInvocation(getCommandOutputInput)
	if err != nil {
		fmt.Println("Warn: error occurred when getting command output:", err)
		return "", err
	}

	if resultCommandOutput == nil {
		fmt.Println("Error: resultCommandOutput is nil")
		return "", fmt.Errorf("resultCommandOutput is nil")
	}

	output := *resultCommandOutput.StandardOutputContent
	return output, nil
}

```
