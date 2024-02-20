import React, {useState, useEffect} from 'react'
import { useNavigate } from "react-router-dom"

const Module1 = () => {
  const navigate = useNavigate();
  const [pageName, setPageName] = useState('')
  const [pageTitle, setPageTitle] = useState('')
  const [pageDescription, setPageDescription] = useState('')

  useEffect(() => {
    if (!window.sessionStorage.getItem("auth")) navigate('/unauthorized')
    fetch('http://localhost:8000/pages/page/1')
    .then(res => res.json())
    .then(data => {
        console.log(data)
        setPageName(data.page.page_name)
        setPageTitle(data.page.page_title)
        setPageDescription(data.page.page_description)
    })
    .catch(error => console.error(error));
}, []);

const axios = require('axios');

async function fplToDatabase() {
  // Navigate to FPL website
  const url = 'https://fantasy.premierleague.com/api/bootstrap-static/';

  // Get raw data dump from FPL website
  try {
    const response = await axios.get(url);
    const jsonBlob = response.data;

    // Get only a subset of the Player Info json blob imbedded in the response
    const playerJsonBlob = jsonBlob['elements'];

    // Create a map of positions using their id and shortname
    const positionJsonBlob = jsonBlob['element_types'];
    const posMap = positionJsonBlob.reduce((map, pos) => {
      map[pos['id']] = pos['singular_name_short'];
      return map;
    }, {});

    // Create a map of teams using their id and shortname
    const teamJsonBlob = jsonBlob['teams'];
    const teamMap = teamJsonBlob.reduce((map, team) => {
      map[team['id']] = team['short_name'];
      return map;
    }, {});

    // Get just the columns that we care about
    const playerDF = playerJsonBlob.map((player) => ({
      id: player['id'],
      first_name: player['first_name'],
      second_name: player['second_name'],
      team: teamMap[player['team']],
      points_per_game: player['points_per_game'],
      total_points: player['total_points'],
      goals_scored: player['goals_scored'],
      assists: player['assists'],
      clean_sheets: player['clean_sheets'],
      form: player['form'],
      penalties_missed: player['penalties_missed'],
      yellow_cards: player['yellow_cards'],
      red_cards: player['red_cards'],
      saves: player['saves'],
      chance_of_playing_next_round: player['chance_of_playing_next_round'],
    }));

    // Iterate over the players and post them to the specified endpoints
    for (const player of playerDF) {
      try {
        // Post player data to create player endpoint
        await axios.post('/users/create_player/', player);

        // Post team data to create team endpoint
        const teamData = { team_name: player['team'] };
        await axios.post('/users/create_team/', teamData);
      } catch (error) {
        console.error('Error posting data:', error.message);
      }
    }
  } catch (error) {
    console.error('Error fetching data from FPL API:', error.message);
  }
}


  return (
    <div>

      <h1>CS415 Private Page - Module 1</h1>
      <p><font color="white">This is only accessible when logged in</font></p>

        <h2>{pageName}</h2>
        <p><b>{pageTitle}</b></p>
        <p><font color='white'>{pageDescription}</font></p>
    </div>

  )
}

export default Module1