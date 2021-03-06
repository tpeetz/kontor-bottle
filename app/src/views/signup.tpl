<!DOCTYPE html>
<html>
<head>
<title>Kontor</title>
<link rel="stylesheet" href="/css/kontor.css">
</head>
<body>
  <header>Kontor</header>
  <nav><ul>
    <li><a href="/">Kontor</a></li>
    <li><a href="/comics">Comics</a></li>
    <ul>
      <li><a href="/comics/artist">Artists</a></li>
      <li><a href="/comics/publisher">Publishers</a></li>
    </ul>
    <li><a href="/library">B&uuml;cher</a></li>
    <li><a href="/medien">Medien</a></li>
    <li><a href="/tradingcards">Trading Cards</a></li>
  </ul></nav>
  <main role="main">
    <details>
    <h2>Signup</h2>
    <form method="post">
      <table>
        <tr><td class="label">Username</td>
          <td><input type="text" name="username" value="{{username}}"></td>
          <td class="error">{{username_error}}</td>
        </tr>
        <tr>
          <td class="label">Password</td>
          <td><input type="password" name="password" value=""></td>
          <td class="error">{{password_error}}</td>
        </tr>
        <tr>
          <td class="label">Verify Password</td>
          <td><input type="password" name="verify" value=""></td>
          <td class="error">{{verify_error}}</td>
        </tr>
        <tr>
          <td class="label">Email (optional)</td>
          <td><input type="text" name="email" value="{{email}}"></td>
          <td class="error">{{email_error}}</td>
        </tr>
      </table>
      <input type="submit">
    </form>
    </details>
  </main>
  <footer>
%if (username == None):
    <a href="/login">Login</a>
%end
%if (username != None):
    <a href="/logout">{{username}}</a>
%end
    <p>Ingenieurb&uuml;ro Thomas Peetz</p>
  </footer>
</body>
</html>
