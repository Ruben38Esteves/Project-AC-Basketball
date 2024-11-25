import pandas as pd

def get_rookie_averages(year, players_teams_df):
    # Initialize a dictionary to store the average values for each column
    averages_dict = {}

    # Iterate over each year from 1 to the given year
    for y in range(1, year + 1):
        # Get the list of players for the current year and the previous year
        current_year_players = set(players_teams_df[players_teams_df['year'] == y]['playerID'])
        previous_year_players = set(players_teams_df[players_teams_df['year'] == y - 1]['playerID'])
        
        # Find rookies by taking the difference between the current year players and previous year players
        rookies = current_year_players - previous_year_players
        
        # Filter the dataframe to include only rookies
        rookies_df = players_teams_df[players_teams_df['playerID'].isin(rookies)]
        
        # Calculate the average value for each column (excluding 'playerID' and 'year')
        averages = rookies_df.drop(columns=['playerID', 'year']).mean()
        
        # Store the averages in the dictionary with the year as the key
        averages_dict[y] = averages

    # Convert the dictionary to a DataFrame
    averages_df = pd.DataFrame(averages_dict).transpose()
    
    # Calculate the overall average for all years
    overall_averages = averages_df.mean()
    
    # Add the overall averages as a new row in the DataFrame
    averages_df.loc['Overall'] = overall_averages
    
    return averages_df
