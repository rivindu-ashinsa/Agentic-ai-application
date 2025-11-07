# Project Hazel

## Overview

Project Hazel is a cutting-edge AI companion designed to enhance mental wellness, support smart learning, foster meaningful connections, and improve focus. This repository contains the landing page for Project Hazel, showcasing its features, technology stack, team, and contact information through a responsive, interactive web interface.

## Key Features

- **Interactive Navigation**: Smooth scrolling navigation bar with links to Home, About, Team, and Contact sections.
- **Hero Section**: Engaging introduction with animated elements and a call-to-action button.
- **Vision Section**: Four key focus areas: Mental Wellness, Smart Learning, Meaningful Connections, and Focus Enhancement, displayed in a grid layout.
- **About Section**: Information about Hazel's origins and purpose, with paired images and text.
- **Features Carousel**: A 3D-style slider highlighting unique features such as physical presence and various modes, with manual and automatic navigation, keyboard, and touch support.
- **Technology Stack**: Badge display of integrations like Raspberry Pi, Gemini AI, MQTT, and others.
- **Team Section**: Grid layout showcasing team members with photos, names, and roles.
- **Contact Section**: Cards for email, location, and social media links with icons and animations.
- **Responsive Design**: Mobile-friendly layouts with animations, hover effects, and fade-in transitions.

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Libraries/Frameworks**:
  - Bootstrap 5.3.0 (for responsive design and components)
  - Font Awesome 6.4.0 (for icons)
- **Hardware/Integrations** (as highlighted in the project):
  - Raspberry Pi
  - Gemini AI
  - MQTT
  - Other technologies (e.g., for modes and presence)
- **Styling**: Custom CSS with Flexbox, Grid, and animations
- **Assets**: Local images (PNG/JPG in `./pics/` directory)

## Project Structure

```
project-hazel/
├── landing_page/
│   ├── index.html           # Main HTML file for the landing page
│   ├── Landing_Page.css     # Custom stylesheets with color variables and animations
│   └── Landing_Page.js      # JavaScript for interactivity (carousel, animations, navigation)
├── pics/                     # Directory for image assets (logo, hero image, team photos, etc.)
│   ├── logo.png
│   ├── pic1.jpg
│   ├── pic2.jpg
│   ├── pic3.png
│   ├── member1.png
│   ├── left.png
│   ├── right.png
│   └── ...
└── README.md                 # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/project-hazel.git
   cd project-hazel
   ```

2. Ensure you have a web server or browser with CORS support (e.g., use a local server like Live Server in VS Code for best results).

3. No build process is required. Simply open `landing_page/index.html` in a web browser to view the site.

4. For hosting, upload the files to a web server that serves static content. Ensure the `./pics/` directory is accessible.

## Usage

- **Navigation**: Use the top navbar to jump to sections or scroll naturally to explore.
- **Carousel**: Interact with the features slider via click/tap navigation, keyboard arrows (left/right), or swipe gestures on touch devices. It also auto-advances every 3 seconds.
- **Responsiveness**: The site adapts to different screen sizes; test on mobile devices for optimal viewing.
- **Interactivity**: Elements fade in on scroll, with hover animations for cards and team members.

The page is optimized for modern browsers supporting ES6 JavaScript, CSS Grid, and Flexbox. It relies on CDN links for Bootstrap and Font Awesome, so an internet connection is recommended during initial load.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Make changes and test on multiple devices/browsers.
4. Submit a pull request with a clear description.

Ensure adherence to responsive design principles and accessibility standards.

## License

This project is licensed under the MIT License. See the LICENSE file for details. (Optional: Adjust based on actual license if present.)