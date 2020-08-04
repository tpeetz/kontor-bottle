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
      <table border="1">
        <tr><td>Title</td><td>Current Order</td><td>Completed</td></tr>
        <tr>
%for comic in comics:
          <td><a href="/comics/comic/{{comic['_id']}}">{{comic['title']}}</a></td>
          <td>{{comic['current_order']}}</td>
          <td>{{comic['completed']}}</td>
%end
        </tr>
      </table>
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
