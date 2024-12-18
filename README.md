# flask_project

# Prerequisites
Before running the Flask application, ensure that you have the following softwares and Dependencies installed:
      Python 3.x, MySQL, Flask, Flask-MySQLdb, MySQL-Connector-Python.

**Database Schema**
The application uses a MySQL database with a users table. Here's the schema:

CREATE DATABASE users;

USE users;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    role VARCHAR(50) NOT NULL
);

INSERT INTO users (name, email, role) VALUES
('Chaitanya', 'chaitanya@gmail.com', 'Admin'),
('Ram', 'ram@yahoo.com', 'Manager'),
('Krishna', 'krishna@outlook.com', 'Guest');


# Git Workflow
I used Git as my version control system and GitHub for remote repository hosting. Here's a summary of the recommended Git workflow:

**Clone the Repository**
If you're contributing to the project, the first step is to fork the repository. Then, clone your fork to your local machine.

**Create a Feature Branch**
To keep the main branch clean and stable, create a new branch for each feature or bug fix you work on. This keeps the development process isolated and organized.
The branch name should be descriptive of the feature or fix you're working on.

**Make Changes Locally**
Implement the changes you need in your feature branch. After making changes, use git status to check which files have been modified.

**Stage and Commit Your Changes**
After making changes, stage and commit them with a clear and descriptive commit message.

**Stage the changes**
Follow Commit Message Guidelines for writing clear, concise commit messages.

**Push Your Branch to GitHub**
Once you've committed your changes, push your feature branch to GitHub.

**Create a Pull Request (PR)**
After pushing your branch, create a Pull Request (PR) to merge your changes into the main branch of the repository.
Go to the repository on GitHub and switch to your feature branch.
GitHub will show you a prompt to Compare & pull request. Click it.
In the PR description, clearly describe the changes made, why they were needed, and any related information.
Click Create pull request.

**Review and Address Feedback**
After creating the pull request, team members will review your changes. Be prepared to receive feedback and make adjustments as needed.
If changes are requested, make those changes locally and push them to your branch:

**Merge the PR**
Once the pull request has been reviewed and approved, it will be merged into the main branch.


# How to Contribute
We welcome contributions to this project! Whether you’re fixing bugs, adding new features, or improving documentation, please follow the guidelines below:

1. Fork the Repository
   If you want to contribute, start by forking the repository to your GitHub account:
     Go to the project repository on GitHub.
     Click the Fork button in the top-right corner of the page to create a copy of the repository in your account.
2. Clone Your Fork
   After forking, clone the repository to your local machine:
3. Create a New Branch
   Before starting your work, create a new branch for your feature or fix:
4. Make Changes and Commit
   Work on your changes, then stage and commit them with meaningful messages.
5. Push to Your Fork
   Once you’re happy with your changes, push your branch to your fork:
6. Create a Pull Request
   Go to your repository on GitHub and create a Pull Request (PR) to merge your changes into the original repository.
   Click on Compare & pull request and provide a description of your changes.
   Select main as the base branch and your feature branch as the compare branch.
7. Participate in Code Reviews
   We believe in collaborative development. If you receive feedback on your pull request, address the comments and make the necessary adjustments.

**Commit Message Guidelines**
We follow a standard format for commit messages to maintain consistency in the repository:
  Use imperative tone: "Fix bug", "Add feature".
  Short description (under 50 characters) for the subject.
  Add a detailed description of the change in the body (if needed).
  Example:
      Add user delete button
    - Implemented delete functionality for deleting the user.
    - Added new button to delete the user.

