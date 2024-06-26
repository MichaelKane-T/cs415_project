
    CREATE TABLE User(

    first_name VARCHAR(35), 
    second_name VARCHAR(35),
    pass_word VARCHAR(35), 
    recovery_key VARCHAR(35), 
    date_created DATETIME,
    email VARCHAR(35),
    user_id INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (user_id) 
);

   
    CREATE TABLE UserAddress (
        Address_1 VARCHAR(35), 
        Address_2 VARCHAR(35),
        City VARCHAR(35), 
        user_id INT NOT NULL,
        Zip VARCHAR(35), 
        Country VARCHAR(35), 
        last_date_updated DATETIME,
        email VARCHAR(35),
        user_address_id INT NOT NULL AUTO_INCREMENT,
        PRIMARY KEY (user_address_id), 
        FOREIGN KEY (user_id) REFERENCES User(user_id)
);

    
    CREATE TABLE Team (
    team_name VARCHAR(35), 
    team_points INT,
    log_position INT, 
    team_form FLOAT, 
    strength_overall_home FLOAT,
    strength_overall_away FLOAT,
    win INT,
    loss INT,
    draw INT,
    team_id INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (team_id) 
);


    CREATE TABLE Player (
    player_id INT NOT NULL AUTO_INCREMENT, 
    first_name VARCHAR(35),
    second_name VARCHAR(35),
    points_per_game INT,
    total_points INT,
    goals_scored INT,
    team_id INT NOT NULL,
    assists INT,
    form INT,
    clean_sheets INT,
    chance_of_playing_next_round INT,
    yellow_cards INT,
    red_cards INT,
    saves INT,
    penalties_missed INT,
    PRIMARY KEY (player_id), 
    FOREIGN KEY (team_id) REFERENCES Team(team_id)
);
 
CREATE TABLE UserInfo (
    user_info_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    profile_bio VARCHAR(500),
    profile_picture VARCHAR(100),
    modified_date DATETIME,
    created_date DATETIME,
    PRIMARY KEY (user_info_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE PhoneType (
    phone_type_id INT NOT NULL AUTO_INCREMENT,
    phone_type VARCHAR(10) NOT NULL,
    PRIMARY KEY (phone_type_id)
);

CREATE TABLE UserPhone (
    user_phone_id INT NOT NULL AUTO_INCREMENT,
    phone_type_id INT NOT NULL,
    user_id INT NOT NULL,
    phone_number VARCHAR(10),
    created_date DATETIME,
    is_active BOOLEAN,
    PRIMARY KEY (user_phone_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (phone_type_id) REFERENCES PhoneType(phone_type_id)
);

CREATE TABLE PageData (
    page_data_id INT NOT NULL AUTO_INCREMENT,
    page_name VARCHAR(25) NOT NULL,
    page_title VARCHAR(25) NOT NULL,
    page_description VARCHAR(150) NOT NULL,
    page_picture VARCHAR(100),
    PRIMARY KEY (page_data_id)
);