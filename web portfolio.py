<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Muhammad | Portfolio</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Poppins', sans-serif;
    }
    body {
      background-color: #f7f9fc;
      color: #333;
      line-height: 1.6;
    }
    header {
      background-color: #2d3748;
      color: white;
      padding: 2rem;
      text-align: center;
    }
    header h1 {
      font-size: 2.5rem;
    }
    header p {
      font-size: 1.2rem;
      margin-top: 0.5rem;
    }
    .container {
      max-width: 1000px;
      margin: auto;
      padding: 2rem;
    }
    section {
      margin-bottom: 3rem;
    }
    h2 {
      font-size: 2rem;
      color: #2b6cb0;
      margin-bottom: 1rem;
      border-bottom: 2px solid #bee3f8;
      display: inline-block;
      padding-bottom: 0.5rem;
    }
    .skills, .projects {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 1rem;
    }
    .card {
      background-color: white;
      padding: 1.5rem;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0,0,0,0.05);
      transition: transform 0.3s;
    }
    .card:hover {
      transform: translateY(-5px);
    }
    footer {
      background-color: #2d3748;
      color: white;
      text-align: center;
      padding: 1rem;
      font-size: 0.9rem;
    }
    .contact a {
      display: inline-block;
      margin: 0.5rem 1rem 0 0;
      color: #2b6cb0;
      text-decoration: none;
    }
  </style>
</head>
<body>
  <header>
    <h1>Muhammad Ibrohim Nigmatov</h1>
    <p>Dasturchi | Telegram Bot | Web Ilovalar</p>
  </header>

  <div class="container">
    <section class="about">
      <h2>Men haqimda</h2>
      <p>Men Muhammad, 16 yoshdaman. Python dasturlash tilida ishlayman, Telegram botlar, Excel ilovalari va web loyihalar yarataman. Hozirda Najot Ta'limda Python o‘rganmoqdaman va Excel Masters'da kompyuter savodxonligidan dars beraman.</p>
    </section>

    <section class="skills">
      <h2>Ko'nikmalar</h2>
      <div class="card">Python</div>
      <div class="card">HTML & CSS</div>
      <div class="card">Telegram Bot</div>
      <div class="card">Excel avtomatlashtirish</div>
      <div class="card">Git & GitHub</div>
    </section>

    <section class="projects">
      <h2>Loyihalar</h2>
      <div class="card">
        <h3>HisobotBot</h3>
        <p>Excelga ma'lumot kirituvchi va hisobot yurituvchi Telegram bot. Python va aiogram yordamida yaratilgan.</p>
        <a href="https://github.com/yourusername/HisobotBot" target="_blank">GitHubda ko‘rish</a>
      </div>
      <div class="card">
        <h3>Portfolio Websayti</h3>
        <p>O‘zim haqimdagi portfolio sahifasi. HTML, CSS yordamida yaratilgan.</p>
        <a href="https://yourusername.github.io/portfolio" target="_blank">Saytni ochish</a>
      </div>
    </section>

    <section class="contact">
      <h2>Aloqa</h2>
      <a href="mailto:youremail@gmail.com">Email: youremail@gmail.com</a>
      <a href="https://t.me/yourtelegram" target="_blank">Telegram: @yourtelegram</a>
    </section>
  </div>

  <footer>
    &copy; 2025 Muhammad Ibrohim. Barcha huquqlar himoyalangan.
  </footer>
</body>
</html>
