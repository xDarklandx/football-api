<h3> Football League API Documentation </h3>
<br>
<h2> Introduction </h2>
<br>
<p> The Football League API allows you to retrieve, store, update, and delete information about matches played in the league. Additionally, it provides functionality to track and store the champions of each season.

With the Football League API, you can:

<ul>
<li>Retrieve match details such as scores, team lineups, and match statistics.</li>
<li>Store new match data, including scores, dates, and participating teams.</li>
<li>Update existing match information, such as editing scores or modifying team lineups.</li>
<li>Delete match records when necessary.</li>
<li>Track and store the champion of each season, allowing you to easily retrieve and display the winning team for any given season.</li>
<li>Whether you need to fetch match data for analysis, maintain accurate league records, or showcase the champions of past seasons, the Football League API offers a comprehensive solution to manage and access this information programmatically.</li>
</ul>

Please note that specific endpoint details and request/response formats would be further elaborated in the API documentation. </p>
<br>

<h2>Authentication</h2>
<br>
<p> Authentication is not required to access the Football League API. </p>
<br>
<h2>Endpoints</h2>
<br>
<h5>1. Get match</h5>
<b> Endpoint: '/match' </b>
<br>
<b> Method: GET </b>
<br>
<p><b>Description:</b> Retrieves the match information for a specified season and matchId </p>
<h5>Parameters:</h5>
<br>
<p>
<ul>
<li><b>'seasonId'</b>: (required): Season ID</li>
<li><b>'sortKey'</b>: (required): Match ID</li>
</ul>
</p>
<h5>Example Request: </h5>
<p> GET /match?seasonId=season-1&sortKey=match-1 </p>
<h5>Example Response: </h5>
<p> {
    "seasonId": "season-1",
    "result": {
        "goalsLocal": "3",
        "localTeam": "Atletico de Madrid",
        "matchDate": "11/05/2023",
        "visitTeam": "Villareal",
        "pointsLocal": "3",
        "goalsVisit": "2",
        "pointsVisit": "0"
    },
    "result.localTeam": "Barcelona",
    "localTeam": "Maraton",
    "sortKey": "match-1"
} </p>
