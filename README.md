## Django Page Counter (Session Management)

A clean, minimalist Django web application that tracks and displays the number of times a page has been visited by a user.
This project demonstrates backend state management using **Django Sessions and Cookies**.

## ⚡ Features

- **Session-Based Tracking:** Counts views per user session accurately without needing a heavy database setup for temporary tracking.
- **Auto-Expiry:** Sessions are configured to expire automatically after 10 seconds of inactivity (`request.session.set_expiry(10)`).
- **Responsive UI:** A sleek, dark-themed frontend with smooth hover animations and a responsive design using CSS `clamp()`.

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3 (Flexbox, Fluid Typography)
- **Icons:** Font Awesome CDN
