
---

#### Step-by-Step Guide: How to Enable DLHC in a SaaS Database

#### **Prerequisites**
- AWS SaaS database created in your AWS account.
- Valid IAM role with the `AmazonEC2ContainerServiceforEC2Role` policy attached.
- Docker installed on the instance.
- Certificates and secrets created and securely stored.

---

### **Step 1: Install Docker and ECS Agent**

1. **Update system packages:**
   ```bash
   sudo apt update -y
   sudo apt install -y docker
   sudo service docker start
   ```

2. **Download and install ECS agent:**
   - For systems with `.deb` package manager:
     ```bash
     curl -O https://s3.us-west-2.amazonaws.com/amazon-ecs-agent-us-west-2/amazon-ecs-init-latest.amd64.deb
     sudo dpkg -i amazon-ecs-init-latest.amd64.deb
     ```

   - For systems with `.rpm` package manager:
     ```bash
     curl -O https://s3.us-west-2.amazonaws.com/amazon-ecs-agent-us-west-2/amazon-ecs-init-latest.x86_64.rpm
     sudo yum localinstall -y amazon-ecs-init-latest.x86_64.rpm
     ```

3. **Enable ECS Agent startup dependency:**
   Edit the ECS service file:
   ```bash
   sudo nano /lib/systemd/system/ecs.service
   ```
   Add the following line under the `[Unit]` section:
   ```ini
   After=cloud-final.service
   ```

4. **Specify ECS cluster:**
   Edit the ECS configuration file:
   ```bash
   sudo nano /etc/ecs/ecs.config
   ```
   Add the cluster name:
   ```plaintext
   ECS_CLUSTER=MyCluster
   ```

5. **Start the ECS service:**
   ```bash
   sudo systemctl start ecs
   ```

6. **Assign permissions to the instance:**
   Ensure your instance’s IAM role has the `AmazonEC2ContainerServiceforEC2Role` policy attached.

---

### **Step 2: Create the Home Directory and User**

1. **Create the home directory `/home/ubuntu/data`:**
   ```bash
   sudo mkdir -p /home/ubuntu/data
   ```

2. **Create a user and group for DLHC (with ID `1010`):**
   ```bash
   sudo groupadd -g 1010 dlhc
   sudo useradd -u 1010 -g 1010 -m -s /bin/bash dlhc
   ```

3. **Ensure the directory ownership is correct:**
   ```bash
   sudo chown -R dlhc:dlhc /home/ubuntu/data
   ```

---

### **Step 3: Certificates Setup**

1. **Copy certificates from Management SaaS:**
   Place the `ssl.crt` and `ssl.key` files into `/home/ubuntu/data`.

2. **Rename certificates:**
   ```bash
   sudo mv /home/ubuntu/data/ssl.crt /home/ubuntu/data/dlhc.crt
   sudo mv /home/ubuntu/data/ssl.key /home/ubuntu/data/dlhc.key
   ```

3. **Set ownership and permissions for the certificates:**
   ```bash
   sudo chown dlhc:dlhc /home/ubuntu/data/dlhc.crt
   sudo chown dlhc:dlhc /home/ubuntu/data/dlhc.key
   ```

---

### **Step 4: Create an S3 Bucket for DLHC Configuration Files**

1. Create an S3 bucket for DLHC configuration files.  
2. Upload a file named `input.env`.  

   **[!] Example format for `input.env`:**
   ```plaintext
   EXASOL_JDBCURL=jdbc:exa:<connection_string>:8563;validateservercertificate=0;logintimeout=10000;logintimeout=10000;
   EXASOL_USERNAME=<user>
   EXASOL_PASSWORD=<password_or_exa_pat_token>
   ```

---

### **Step 5: Create a Task Definition**

1. **Prepare the task definition JSON file:**  
   Save a file named `task-definition.json` with the required contents. Update placeholder values:
   - `<dlhc image>`: Replace with the container image you're using (e.g., `533884745449.dkr.ecr.eu-central-1.amazonaws.com/saas/neptune:0.8.0`).
   - `<bucket_name>`: Replace with your S3 bucket name for environment variables.
   - `<account_id>`: Replace with your AWS account ID.
   - `<private_ip>`: Replace with the private IP of your instance.

2. **Create the task definition:**  
   Run the following command:
   ```bash
   aws ecs create-task-definition --cli-input-json file://task-definition.json
   ```

3. **Register the task definition:**  
   Run the following command:
   ```bash
   aws ecs register-task-definition --cli-input-json file://task-definition.json
   ```

---

### **Step 6: Verify DLHC Setup**

1. **Check the DLHC service health:**
   Use `curl` to verify:
   ```bash
   curl -k https://<private_ip>:8443/actuator/health
   ```

---

