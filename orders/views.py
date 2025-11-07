<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>طلباتي | متجر أدوات السلامة C7</title>
  <style>
    body {
      margin: 0;
      font-family: 'Tahoma', sans-serif;
      background: linear-gradient(135deg, #0d1b2a, #1b263b, #415a77);
      color: #ffffff;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    header {
      background: linear-gradient(90deg, #001233, #003566);
      padding: 15px 30px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 2px 10px rgba(0,0,0,0.4);
    }
    header .logo {
      font-size: 1.6rem;
      font-weight: bold;
      color: #ffcc00;
    }
    nav a {
      color: #ffffff;
      text-decoration: none;
      margin-left: 20px;
      transition: color 0.3s ease;
    }
    nav a:hover {
      color: #ffcc00;
    }

    main {
      flex: 1;
      padding: 40px;
    }

    h1 {
      color: #ffcc00;
      text-align: center;
      margin-bottom: 30px;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      background-color: rgba(255, 255, 255, 0.1);
      border-radius: 10px;
      overflow: hidden;
    }

    th, td {
      padding: 12px;
      text-align: center;
      border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    }

    th {
      background-color: rgba(255, 255, 255, 0.15);
      color: #ffcc00;
    }

    tr:hover {
      background-color: rgba(255, 255, 255, 0.15);
    }

    .status {
      padding: 5px 10px;
      border-radius: 8px;
      font-size: 0.9rem;
      font-weight: bold;
    }

    .status.قيد\ المعالجة { background-color: #ffcc00; color: #001233; }
    .status.مكتمل { background-color: #00c851; color: #fff; }
    .status.ملغي { background-color: #dc3545; color: #fff; }

    footer {
      background-color: #0b132b;
      text-align: center;
      padding: 15px;
      font-size: 0.9rem;
      color: #adb5bd;
      border-top: 1px solid #1b263b;
    }
  </style>
</head>
<body>

  <header>
    <div class="logo">🦺 C7 Safety Store</div>
    <nav>
      <a href="/">الرئيسية</a>
      <a href="/store/">المنتجات</a>
      <a href="/orders/">طلباتي</a>
      <a href="/admin/">لوحة التحكم</a>
    </nav>
  </header>

  <main>
    <h1>طلباتي السابقة</h1>

    <table>
      <thead>
        <tr>
          <th>رقم الطلب</th>
          <th>التاريخ</th>
          <th>الحالة</th>
          <th>المجموع</th>
          <th>المنتجات</th>
        </tr>
      </thead>
      <tbody>
        {% for order in orders %}
        <tr>
          <td>{{ order.id }}</td>
          <td>{{ order.date }}</td>
          <td><span class="status {{ order.status }}">{{ order.status }}</span></td>
          <td>{{ order.total }} ريال</td>
          <td>{{ order.items|join:", " }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </main>

  <footer>
    © 2025 متجر أدوات السلامة C7 — جميع الحقوق محفوظة.
  </footer>

</body>
</html>
