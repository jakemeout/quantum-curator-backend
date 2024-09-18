## Prerequisites

Before you begin, ensure you have the following:

- **AWS Account**: Access to AWS services.
- **AWS CLI**: Installed and configured with your AWS credentials.
- **SSH Key Pair**: For accessing the EC2 instance.
- **GitHub Repository**: For storing your application code.
- **Python 3.8+**: Installed locally for development.

## Setting Up PostgreSQL on AWS RDS

1. **Create an RDS Instance**

   - Log in to the AWS Management Console.
   - Navigate to RDS and click on "Create database".
   - Select PostgreSQL and use the following settings:
     - **DB instance identifier**: `fastapi-db`
     - **Master username**: `admin`
     - **Master password**: `your_password`
     - **Instance type**: `db.t3.micro` (for development)
     - **Storage**: 20GB
     - **Public access**: Enabled
   - Click "Create database" and wait for the instance to be available.

2. **Configure Security Groups**

   - Go to EC2 Dashboard > Security Groups.
   - Edit the security group associated with your RDS instance.
   - Add an inbound rule to allow traffic on port `5432` from your IP or EC2 instance.

3. **Connect to the RDS Instance**

   - Use the `psql` command to connect:
   ```bash
   psql -h <your-db-endpoint>.rds.amazonaws.com -U admin -d postgres
