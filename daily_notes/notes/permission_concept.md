---
id: permission_concept
aliases: []
tags: []
---

Control Tower Group

Purpose

Summary

Authorized Users

Authorized Approver

SystemSupport  

The purpose is to enable system support personnel to efficiently access, monitor, and manage necessary AWS resources while preventing excessive permissions. It ensures support staff can perform essential tasks such as monitoring, listing resources, describing configurations, and managing instances, crucial for maintaining the integrity and performance of AWS services within the organization.

The permissions allow for descriptive, listing, and read-only operations across various AWS services, facilitating system support and monitoring tasks.

AbdiMohamed

BogdanMihai

ElsaPulido

FardinSabzi

GeorgHenne

GeraldChibuzorOti

LuisFelipeCarrilloMoreno

MihailAlexandris

StefanReich

ViorelBosneac

VitaliiShilin                             

Swen Elges

StagingSaaSAccess

The purpose is to enable an administrator to manage IAM roles by creating new roles, retrieving details about existing roles, and listing policies attached to any role. This is particularly useful in a SaaS administrative context where managing user roles and their associated permissions within the AWS environment is necessary.

The permissions allow a user or role to perform specific actions related to AWS IAM roles, such as creating new roles, retrieving details about existing roles, and listing attached policies.

Andrew MacLean

AvantikaSikand

Haibo Lei 

Irakli Bejelidze 

Mihai Dinca 

Sebastian Nehls 

Thomas Ubensee 

Vahid Zangeneh

 

SecurityReadAccess

The purpose is to give full access to Security Hub's features and resources to help manage security and compliance in AWS. This is usually for users, roles, or services that need complete control and visibility of Security Hub.

The permissions allow all Security Hub actions on all resources, providing broad access to manage and use AWS Security Hub

Andrew MacLean  

Andrew MacLean

SaaS-Admin-Group 

The purpose is to let an administrator manage IAM roles by creating new ones, viewing details about existing roles, and listing policies attached to any role. This is useful for managing user roles and permissions in a SaaS environment.

 The policy grants permiss
ions to a user or a role to perform specific actions related to AWS IAM roles. 

Andrew MacLean 

Mihai Dinca

Andrew MacLean

RnD

The purpose is to set up permissions for managing and operating AWS services like CloudFormation, EC2, and Lambda, allowing control over resources, settings, and monitoring

The permissions provide broad read, list, describe, and some write access across many AWS services, essential for managing and monitoring AWS environments.

Andrew MacLean 

Haibo Lei

Mihai Dinca

OleksandrKozachuk

Andrew MacLean

ProductSupport 

The purpose is to grant broad read and execute permissions across many AWS services, allowing tasks like listing resources, describing their states, starting/stopping EC2 instances, and managing SSM commands and sessions. This is useful for an auditing or monitoring service that needs to gather and act on information without making any changes.

The permissions allow listing, describing, and getting information about resources in various AWS services. It also permits basic actions like starting and stopping EC2 instances and managing SSM sessions and commands.

Aleksandr Lipatev 

John Askew 

Juergen Loebel 

Nisha Yadav 

Peggy Schmidt Mittenzwei

Swen Elges

ProductionEngineeringTeam 

The purpose is to allow the designated user or role to fully manage and configure AWS services and resources, ensuring they have the access needed to perform all administrative tasks without restrictions

 This policy includes permissions to perform any a
ction on all AWS resources and services.

Andrew MacLean 

Edis Shabi 

Robert Rex

Andrew MacLean

EnterpriseServices

The purpose is to give an entity full access and control over key AWS services for managing resources, configuring security, and orchestrating infrastructure. It includes permissions for managing storage, creating and handling infrastructure as code, overseeing instances, performing user role operations, and managing encryption keys

The document outlines an IAM policy that grants various permissions to interact with AWS services. It includes sections with unique identifiers and lists of allowed actions for specific resources.

Dren Daka 

Marcel Kempken

 

Development    

 Control AWS actions by restricting them to specific regions and enhance security by preventing the creation of new IAM users, thereby avoiding unauthorized access and maintaining a manageable IAM structure.

 Grants permissions to perform all actions on all resources but restricts them to specific AWS regions. It also explicitly denies the creation of new IAM users across all resources

Andrew MacLean 

Haibo Lei 

Mihai Dinca 

Oleksandr Kozachuk

Andrew MacLean

CostExplorerView

The primary purpose of this policy is to allow users to effectively monitor, analyze, and manage their AWS costs and usage. This is achieved by permitting actions such as accessing cost and usage reports, creating 
and describing reports, viewing billing details, and managing purchase orders and tax-related documents. Ensuring comprehensive visibility and control over AWS expenditures facilitates better financial planning and
 cost optimization.

The `costexplorerview.json` policy is a permissions document designed to grant users comprehensive access to various AWS Cost Explorer, billing, and invoicing services. The policy is structured to enable viewing, r
etrieving, and managing cost and billing data, including cost forecasts, usage reports, savings plans, purchase orders, and tax documents.

Andreas Bonet 

Andrew MacLean

Andreas Bonet / Andrew Maclean

CostExplorerAccess 

This summary gives a comprehensive overview of the goals and benefits of the cost explorer policy in relation to an ISO ticket. It does not delve into the specifics of the data but encapsulates the overall intent a
nd utility of the policy.

The primary purpose of the ISO ticket addressed in the `cost_explorer.json` file is to enhance cost visibility and management by analyzing and reporting cloud service usage within an organization. This helps in ide
ntifying cost optimization opportunities and ensuring that cloud expenses align with the organization's budgeting and compliance requirements.

Sebastian Nehls

Andrew MacLean

ConsumptionReport 

The purpose of the group grant is to authorize access to S3 buckets, primarily for listing and retrieving consumption and SLA (Service Level Agreement) reports.

Ensures the group can access and manage crucial reporting data while maintaining an overview of all available S3 storage resources within the account.

Andreas Bonet 

Alen Alex

Andreas Bonet

AthenaAccess

 this policy enables broad access to Athena and Glue for data processing and provides specific access to required S3 buckets for managing customer reports and cost analysis data.

the permissions for accessing Amazon Athena, AWS Glue, and specific Amazon S3 buckets. 

Andreas Bonet

Andreas Bonet

 ServiceQuotaGroup

The primary purpose of this policy is to allow users or applications the ability to manage and monitor AWS service quotas, which includes listing current quotas, viewing default and custom quotas, requesting increa
ses, and accessing relevant CloudWatch metrics, as well as interacting with AWS Support.

The policy allows for listing, viewing default and specific quotas, requesting q
uota increases, retrieving CloudWatch metric data, and describing the organization. 

Andrew MacLean 

Haibo Lei 

Mihai Dinca 

Andrew MacLean

 BillingAccessGroup 

In summary, "AWSSupportAccess" facilitates support-related interactions, while the "Billing" policy offers control over billing and financial management within AWS.

 policy provides the necessary permissions for viewing and managing AWS Support Center resources, such as support c
ases, AWS Trusted Advisor, and AWS Personal Health Dashboard, without granting full administrative access to other AWS resources. It provides users with access to view and manage billing information and invoices, enabling them to monitor and control AWS spending. 
The policy ensures that users can handle all financial aspects of their AWS account without interfering with other operational functionalities.

Andreas Bonet 

Alen Alex

Andreas Bonet
