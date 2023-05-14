<h1> Football League API Documentation </h1>
<h2> Introduction </h2>
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
<h3>1. Get match</h3>
<b> Endpoint: '/match' </b>
<br>
<b> Method: GET </b>
<br>
<p><b>Description:</b> Retrieves the match information for a specified season and match </p>
<h4>Parameters:</h4>
<p>
<ul>
<li><b>'seasonId'</b>: (required): Season ID</li>
<li><b>'sortKey'</b>: (required): Match ID</li>
</ul>
</p>
<h4>Example Request: </h4>
<p> GET /match?seasonId=season-1&sortKey=match-1 </p>
<h4>Example Response: </h4>
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

<h3>2. Save match</h3>
<b> Endpoint: '/match' </b>
<br>
<b> Method: POST </b>
<br>
<p><b>Description:</b> Saves the match information for a specified season and match </p>
<h4>Parameters:</h4>
<p>
<ul>
<li><b>'seasonId'</b>: (required): Season ID</li>
<li><b>'sortKey'</b>: (required): Match ID</li>
<li><b>'result'</b>: (required): Match Information </li>
</ul>
</p>
<h4>Example Request: </h4>
<p> POST /match <br>
    Content-Type: application/json <br>
    {
    "seasonId": "season-1",
    "sortKey": "match-1",
    "result": {
        "matchDate": "11/05/2023",
        "localTeam": "Real Madrid",
        "visitTeam": "Barcelona",
        "goalsLocal": "3",
        "goalsVisit": "2",
        "pointsLocal": "3",
        "pointsVisit": "0"
    }
}
</p>
<h4>Example Response: </h4>
<p> {
    "Operation": "SAVE",
    "Message": "SUCCESS",
    "Item": {
        "seasonId": "season-3",
        "sortKey": "match-1",
        "result": {
            "matchDate": "11/05/2023",
            "localTeam": "Real Madrid",
            "visitTeam": "Barcelona",
            "goalsLocal": "3",
            "goalsVisit": "2",
            "pointsLocal": "3",
            "pointsVisit": "0"
        }
    }
} </p>

<h3>3. Modify match</h3>
<b> Endpoint: '/match' </b>
<br>
<b> Method: PATCH </b>
<br>
<p><b>Description:</b> Updates the match information for a specified season and match </p>
<h4>Parameters:</h4>
<p>
<ul>
<li><b>'seasonId'</b>: (required): Season ID</li>
<li><b>'sortKey'</b>: (required): Match ID</li>
<li><b>'updateKey'</b>: (required): Field name to be updated (result) </li>
<li><b>'updateValue'</b>: (required): Value in json format to be updated </li>
</ul>
</p>
<h4>Example Request: </h4>
<p> PATCH /match <br>
    Content-Type: application/json <br>
    {
	"seasonId": "season-1",
	"sortKey": "match-1",
	"updateKey": "result",
	"updateValue": {
        "localTeam": "Atletico de Madrid"
    }
}
</p>
<h4>Example Response: </h4>
<p> {
    "Operation": "UPDATE",
    "Message": "SUCCESS",
    "UpdatedItem": {
        "seasonId": "season-1",
        "sortKey": "match-1"
        "result": {
            "matchDate": "11/05/2023",
            "localTeam": "Atletico de Madrid",
            "visitTeam": "Barcelona",
            "goalsLocal": "3",
            "goalsVisit": "2",
            "pointsLocal": "3",
            "pointsVisit": "0"
        },
    }
} </p>

<h3>4. Delete match</h3>
<b> Endpoint: '/match' </b>
<br>
<b> Method: DELETE </b>
<br>
<p><b>Description:</b> Deletes the match information for a specified season and match </p>
<h4>Parameters:</h4>
<p>
<ul>
<li><b>'seasonId'</b>: (required): Season ID</li>
<li><b>'sortKey'</b>: (required): Match ID</li>
</ul>
</p>
<h4>Example Request: </h4>
<p> DELETE /match <br>
    Content-Type: application/json <br>
    {
    "seasonId": "season-3",
    "sortKey": "match-1"
}
</p>
<h4>Example Response: </h4>
<p> {
    {
    "Operation": "DELETE",
    "Message": "SUCCESS",
    "DeletedItem": {
        "seasonId": "season-3",
        "result": {
            "goalsLocal": "3",
            "localTeam": "Real Madrid",
            "matchDate": "11/05/2023",
            "visitTeam": "Barcelona",
            "pointsLocal": "3",
            "goalsVisit": "2",
            "pointsVisit": "0"
        },
        "sortKey": "match-1"
    }
},
} </p>

<h3>5. Get all matches</h3>
<b> Endpoint: '/matches' </b>
<br>
<b> Method: GET </b>
<br>
<p><b>Description:</b> Retrieves the matches information for a all the seasons, matches, and champions </p>
<h4>Parameters:</h4>
<p>
<ul>
<li><b>None</b></li>
</ul>
</p>
<h4>Example Request: </h4>
<p> GET /matches </p>
<h4>Example Response: </h4>
<p> {
    "matches": [
        {
            "seasonId": "season-1",
            "result": {
                "championName": "Real Madrid",
                "championPoints": "11"
            },
            "sortKey": "champion"
        },
        {
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
        },
        {
            "seasonId": "season-1",
            "result": {
                "goalsLocal": "2",
                "localTeam": "Real Sociedad",
                "matchDate": "11/05/2023",
                "visitTeam": "Villareal",
                "pointsLocal": "1",
                "goalsVisit": "2",
                "pointsVisit": "1"
            },
            "sortKey": "match-2"
        },
        {
            "seasonId": "season-2",
            "result": {
                "goalsLocal": "3",
                "localTeam": "Bayern",
                "matchDate": "11/05/2023",
                "visitTeam": "Dortmund",
                "pointsLocal": "3",
                "goalsVisit": "1",
                "pointsVisit": "0"
            },
            "sortKey": "match-1"
        }
    ]
} </p>

<h3>6. Get champion</h3>
<b> Endpoint: '/champion' </b>
<br>
<b> Method: GET </b>
<br>
<p><b>Description:</b> Retrieves the champion information for a specified season </p>
<h4>Parameters:</h4>
<p>
<ul>
<li><b>'seasonId'</b>: (required): Season ID</li>
<li><b>'sortKey'</b>: (required): 'champion'</li>
</ul>
</p>
<h4>Example Request: </h4>
<p> GET /match?seasonId=season-1&sortKey=champion </p>
<h4>Example Response: </h4>
<p> {
    "seasonId": "season-1",
    "result": {
        "championName": "Real Madrid",
        "championPoints": "11"
    },
    "sortKey": "champion"
} </p>

<h3>7. Save chmapion</h3>
<b> Endpoint: '/champion' </b>
<br>
<b> Method: POST </b>
<br>
<p><b>Description:</b> Saves the champion information for a specified season </p>
<h4>Parameters:</h4>
<p>
<ul>
<li><b>'seasonId'</b>: (required): Season ID</li>
<li><b>'sortKey'</b>: (required): 'champion'</li>
<li><b>'result'</b>: (required): Champion information </li>
</ul>
</p>
<h4>Example Request: </h4>
<p> POST /champion <br>
    Content-Type: application/json <br>
    {
    "seasonId": "season-2",
    "sortKey": "champion",
    "result": {
        "championName": "Barcelona",
        "championPoints": "12"
    }
}
</p>
<h4>Example Response: </h4>
<p> {
    "Operation": "SAVE",
    "Message": "SUCCESS",
    "Item": {
        "seasonId": "season-2",
        "sortKey": "champion",
        "result": {
            "championName": "Barcelona",
            "championPoints": "12"
        }
    }
} </p>

<h3>8. Modify champion</h3>
<b> Endpoint: '/champion' </b>
<br>
<b> Method: PATCH </b>
<br>
<p><b>Description:</b> Updates the champion information for a specified season </p>
<h4>Parameters:</h4>
<p>
<ul>
<li><b>'seasonId'</b>: (required): Season ID</li>
<li><b>'sortKey'</b>: (required): 'champion'</li>
<li><b>'updateKey'</b>: (required): Field name to be updated (result) </li>
<li><b>'updateValue'</b>: (required): Value in json format to be updated </li>
</ul>
</p>
<h4>Example Request: </h4>
<p> PATCH /match <br>
    Content-Type: application/json <br>
    {
	"seasonId": "season-2",
	"sortKey": "champion",
	"updateKey": "result",
    "updateValue": {
        "championName": "Real Madrid"
    }
}
</p>
<h4>Example Response: </h4>
<p> {
    "Operation": "UPDATE",
    "Message": "SUCCESS",
    "UpdatedItem": {
        "seasonId": "season-2",
        "result": {
            "championName": "Real Madrid",
            "championPoints": "12"
        },
        "sortKey": "champion"
    }
} </p>

<h3>9. Delete champion</h3>
<b> Endpoint: '/champion' </b>
<br>
<b> Method: DELETE </b>
<br>
<p><b>Description:</b> Deletes the champion information for a specified season </p>
<h4>Parameters:</h4>
<p>
<ul>
<li><b>'seasonId'</b>: (required): Season ID</li>
<li><b>'sortKey'</b>: (required): 'champion'</li>
</ul>
</p>
<h4>Example Request: </h4>
<p> DELETE /match <br>
    Content-Type: application/json <br>
    {
    "seasonId": "season-2",
    "sortKey": "champion"
}
</p>
<h4>Example Response: </h4>
<p> {
    {
    "Operation": "DELETE",
    "Message": "SUCCESS",
    "DeletedItem": {
        "seasonId": "season-2",
        "result": {
            "championName": "Real Madrid",
            "championPoints": "12"
        },
        "sortKey": "champion"
    }
},
} </p>
