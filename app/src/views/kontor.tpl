<!DOCTYPE html>
<html>
<head>
<title>Kontor</title>
<link rel="stylesheet" href="css/kontor.css">
</head>
<body>
  <header>Kontor</header>
  <nav><ul>
    <li><a href="/">Kontor</a></li>
    <li><a href="/comics">Comics</a></li>
    <li><a href="/library">B&uuml;cher</a></li>
    <li><a href="/medien">Medien</a></li>
    <li><a href="/tradingcards">Trading Cards</a></li>
  </ul></nav>
  <main role="main">
    <details>
    </details>
  </main>
%if (username == None):
  <footer><a href="/login">Login</a><p>Ingenieurb&uuml;ro Thomas Peetz</p></footer>
%end
%if (username != None):
  <footer><a href="/logout">{{username}}</a><p>Ingenieurb&uuml;ro Thomas Peetz</p></footer>
%end
</body>
</html>
