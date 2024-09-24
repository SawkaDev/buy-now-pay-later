# Buy Now Pay Later Platform

This repository contains the source code for a simple Buy Now Pay Later platform, which includes multiple microservices and a frontend dashboard.

## Table of Contents

- [Screenshots and Demo](#screenshots-and-demo)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Services](#services)
  - [API Gateway](#api-gateway)
  - [Credit Service](#credit-service)
  - [Loan Service](#loan-service)
  - [Merchant Integration Service](#merchant-integration-service)
  - [User Service](#user-service)
- [Frontend](#frontend)
- [Setup and Running](#setup-and-running)
  - [Docker](#docker)
  - [Docker Compose](#docker-compose)
  - [Viewing Redis Tokens](#viewing-redis-tokens)
  - [Helpful Commands](#helpful-commands)

## Screenshots and Demo

- You can view screenshots of the platform [here](./assets).
- A demo video is available [TBD](#).

![
Architecture Diagram](./assets/architecture.png)

## Features

- **BNPL Dashboard**:

  - Merchants can create accounts.
  - Create API keys.
  - Set up webhook endpoints.
  - View their customer loans and their status.

- **Demo Frontend Sample Shop**:
  - Mock checkout process.
  - Creates a checkout session.
  - Backend performs credit underwriting and fraud detection.
  - Issues available loans for the user to select.

## Technologies Used

The platform leverages a variety of technologies to deliver a robust and scalable solution:

- **Backend**:
  - Flask: A lightweight WSGI web application framework.
  - gRPC: A high-performance, open-source universal RPC framework used for communication between microservices.
  - PostgreSQL: Each service has its own PostgreSQL database.
  - Redis: Used for user sessions and caching of data.
  - Rate Limiting: Implemented to control the rate of requests sent or received by the services to ensure fair usage and prevent abuse.
  - JWT Auth: JSON Web Tokens for secure authentication and authorization.
- **Frontend**:
  - Next.js: A React framework for server-side rendering and static site generation.
  - React: A JavaScript library for building user interfaces.
  - React Hook Form: A library for managing form state in React.
  - React Query: A library for fetching, caching, and updating data in React applications.
  - Material UI: A popular React UI framework.

## Project Structure

- backend/
  - api-gateway/
  - credit-service/
  - loan-service/
  - merchant-integration-service/
  - user-service/
- frontend/
  - merchant-bnpl-dashboard/
  - merchant-shop-sample/

## Services

### API Gateway

The API Gateway handles incoming requests and routes them to the appropriate microservices.

### Credit Service

The Credit Service is responsible for handling all credit-related operations within the platform. This includes:

- **Credit Underwriting**: Assessing the creditworthiness of users applying for loans.
- **Credit Scoring**: Calculating a credit score based on user data and transaction history.
- **Credit Limits**: Setting and managing credit limits for users.
- **Credit History**: Maintaining a record of users' credit transactions and histories.
- **Integration with External Credit Bureaus**: Mock communicating with external credit bureaus to fetch and update credit information.

### Loan Service

The Loan Service handles loan-related operations. This includes:

- **Loan Origination**: The process of creating new loans, including application, approval, and disbursement.
- **Loan Management**: Managing the lifecycle of loans, including repayments, interest calculations, and adjustments.
- **Loan Repayment**: Tracking and processing loan repayments from users.
- **Loan Status Monitoring**: Monitoring the status of loans to ensure timely repayments and flagging any delinquencies.
- **Interest Calculation**: Calculating interest on outstanding loans based on predefined rates and schedules.

### Merchant Integration Service

The Merchant Integration Service manages merchant-related operations. This includes:

- **Merchant Onboarding**: Facilitating the process for new merchants to join the platform, including registration, verification, and approval.
- **API Key Management**: Allowing merchants to generate and manage API keys for integrating their systems with the platform.
- **Webhook Management**: Enabling merchants to set up and manage webhook endpoints for receiving real-time notifications about transactions and other events.
- **Merchant Dashboard**: Providing a user-friendly interface for merchants to view and manage their accounts, transactions, and customer loans.
- **Transaction Monitoring**: Tracking and monitoring transactions initiated by merchants to ensure compliance and detect any anomalies.
- **Reporting and Analytics**: Offering detailed reports and analytics to help merchants understand their performance and make informed decisions.

### User Service

The User Service handles user-related operations. This includes:

- **User Registration**: Allowing new users to sign up and create accounts on the platform.
- **User Authentication**: Managing user login and authentication using JWT tokens.
- **User Profile Management**: Enabling users to view and update their profile information.
- **User Session Management**: Handling user sessions and ensuring secure access to the platform.
- **Password Management**: Providing functionality for users to reset and change their passwords.

## Frontend

The frontend consists of a merchant dashboard and a sample shop. Users can add items to their cart and then checkout with the BNPL service.

## Setup and Running

### Docker

Each service has its own Dockerfile. To build and run a service, navigate to the service directory and use the following commands:

```sh
docker build -t <service-name> -f <service-name>.dockerfile .
docker run -p <host-port>:<container-port> <service-name>
```

### Docker Compose

To build and run all services together, use Docker Compose:

```sh
docker-compose up --build
```

This will use the compose.yml file to build and start all services.

### Viewing Redis Tokens

docker exec -it redis redis-cli -a yourredispassword

### Helpful Commands

- docker exec -it db psql -U postgres -d user_service_db
- docker exec -it db psql -U postgres -d api_key_service_db
- \l - view all databases
- \c DATABASE - change to database
- \dt - view all tables for a database
