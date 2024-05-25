# Personal Portfolio Website

## Project Overview
This repository contains the source code for my personal portfolio website, designed to showcase my capabilities and represent my personal brand. This project demonstrates my skills in full-stack web development, leveraging the Python Flask framework and a Bootstrap template.

## Features
- **Customized Portfolio Template:** Utilized the [iPortfolio Bootstrap template](https://bootstrapmade.com/iportfolio-bootstrap-portfolio-websites-template/) to create a sleek and responsive design.
- **Server and Deployment:** Configured and deployed on a Virtual Private Server (VPS) with Ubuntu and Apache to ensure reliable accessibility.
- **Remote Development:** All developments were managed remotely using Linux command line tools and SSH for a streamlined workflow.
- **Flask and Apache Integration:** Integrated the Flask application with Apache using WSGI, ensuring seamless operation and performance.
- **Domain and DNS Configuration:** Acquired and set up `drfoadnajafi.tech` to establish a professional web presence with effective DNS routing.

## Installation and Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/portfolio-website.git
   ```
2. **Install Necessary Packages:**
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-dev libapache2-mod-wsgi-py3
   sudo apt install apache2
   ```
3. **Set Up the Flask Application:**
   Navigate to your project directory and install dependencies:
   ```bash
   cd portfolio-website
   pip3 install -r requirements.txt
   ```
4. **Configure Apache to Serve the Flask App:**
   Modify your Apache configuration files to point to the WSGI entry point of your Flask application.

5. **Restart Apache to Apply Changes:**
   ```bash
   sudo systemctl restart apache2
   ```

## Cost-Effective Strategy
This project leverages open-source technologies to minimize operational costs. The monthly expense for the VPS is approximately $4, with a one-time domain registration fee of $24 for two years.

## Conclusion
This portfolio website is a testament to my ability to design, develop, and deploy a full-stack web application using contemporary technologies in a cost-effective manner. For more information on this project, please contact me or open an issue in this repository.

