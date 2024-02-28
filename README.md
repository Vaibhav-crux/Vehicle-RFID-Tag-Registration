# RFID Tag Management Software

## Overview

This software is designed to streamline the registration and verification process of RFID tags, providing a user-friendly interface for managing vehicle information. The tool is developed using Python and PyQt, with database operations integrated using an Object-Relational Mapping (ORM). The implementation also utilizes Google Cloud Platform (GCP) resources, including Compute Engine, Identity and Access Management (IAM), API & Services, and Container Registry.

## Features

### 1. Login

The software includes a secure login system to ensure authorized access to the RFID tag management system.

### 2. Vehicle Registration

- **Automatic Data Fetch:** When an RFID number is entered, the system automatically retrieves existing data from the database.
- **Field Population:** Data is seamlessly entered into the respective fields for efficient registration.

### 3. Register Vehicle

The tool facilitates the registration of vehicles with ease. Users can input relevant information, and the system ensures a smooth registration process.

### 4. Light and Dark Themes

The software offers both light and dark themes to cater to user preferences. Users can switch between themes for a personalized experience.

## Technologies Used

- **Python:** The core programming language for development.
- **PyQt:** Utilized for creating the graphical user interface (GUI).
- **ORM (Object-Relational Mapping):** Integrated for efficient database operations.
- **Google Cloud Platform (GCP):** Leveraged GCP resources, including Compute Engine, IAM, API & Services, and Container Registry.

## How to Run

To run the RFID Tag Management Software, follow these steps:

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/your_username/rfid-tag-management.git
   ```

2. Install the required dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application.
   ```bash
   python main.py
   ```

4. Access the software through your web browser at http://localhost:8000.

## Screenshots

### Dark Theme
# Login
![Screenshot 2024-02-10 160349](https://github.com/Vaibhav-crux/driver/assets/122672330/9ada2743-2255-47e8-9749-5da17ebae274)
# Registration
![Screenshot 2024-02-10 160404](https://github.com/Vaibhav-crux/driver/assets/122672330/19e98381-b97e-4c4a-b873-1ae29095ad0a)
# Automatic fetch of already existing data from the database when the RFID number found
![Screenshot 2024-02-10 160522](https://github.com/Vaibhav-crux/driver/assets/122672330/92a15a86-5ece-4e36-a1e9-370985bf6df9)
# Data automatically entered in the respective field
![Screenshot 2024-02-10 160603](https://github.com/Vaibhav-crux/driver/assets/122672330/450cb639-1f3e-4fe1-bc58-c2c90386556e)
# Registered 
![Screenshot 2024-02-10 160444](https://github.com/Vaibhav-crux/driver/assets/122672330/bbcc172d-fc36-4559-abc8-bcde8d9177c0)
# Fields in registered
![Screenshot 2024-02-10 160459](https://github.com/Vaibhav-crux/driver/assets/122672330/873b3d4d-4122-4a7a-8a5d-038675f0ec7e)

### Light Theme
![Screenshot 2024-02-10 195523](https://github.com/Vaibhav-crux/driver/assets/122672330/d0931dfe-8e68-4ae8-ab47-e9574a948bec)
![Screenshot 2024-02-10 195538](https://github.com/Vaibhav-crux/driver/assets/122672330/432f1b8d-861f-4679-b8a0-b91ccb884006)
![Screenshot 2024-02-10 195616](https://github.com/Vaibhav-crux/driver/assets/122672330/0542d6f0-f6dd-4faa-80f5-f5473165e513)

