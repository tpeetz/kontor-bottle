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
    <li><a href="/comics/comic">Comics</a></li>
    <ul>
      <li><a href="/comics/artist">Artists</a></li>
      <li><a href="/comics/publisher">Publishers</a></li>
      <li><a href="/comics/storyarc">StoryArcs</a></li>
    </ul>
    <li><a href="/library">B&uuml;cher</a></li>
    <li><a href="/medien">Medien</a></li>
    <li><a href="/tradingcards">Trading Cards</a></li>
  </ul></nav>
  <main role="main">
    <details>
      <ul>
%for storyarc in storyarcs:
        <li><a href="/comics/storyarc/{{storyarc['_id']}}">{{storyarc['title']}}</a></li>
%end
      </ul>
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
