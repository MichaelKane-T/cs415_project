USE cs415website;

CREATE TABLE User(
    user_id int NOT NULL AUTO_INCREMENT,
    first_name varchar(25) NOT NULL,
    last_name varchar(30) NOT NULL,
    email varchar(40) NOT NULL,
    `password` varchar(40) NOT NULL,
    created_date datetime DEFAULT NULL,
    is_active tinyint(1) DEFAULT NULL,
    last_login datetime DEFAULT NULL,
    PRIMARY KEY (user_id),
    UNIQUE (email)
);

CREATE TABLE AddressType (
    address_type_id INT NOT NULL AUTO_INCREMENT,
    address_type VARCHAR(20) NOT NULL,
    PRIMARY KEY (address_type_id)
);

CREATE TABLE UserAddress (
    user_address_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    street_1 VARCHAR(50),
    street_2 VARCHAR(50),
    city VARCHAR(35),
    st VARCHAR(2),
    zip VARCHAR(10),
    country VARCHAR(35),
    address_type_id INT NOT NULL,
    PRIMARY KEY (user_address_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (address_type_id) REFERENCES AddressType(address_type_id)
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
    la VARCHAR(35),
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
    profile_picture VARCHAR(150),
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
    page_name VARCHAR(150) NOT NULL,
    page_title VARCHAR(150) NOT NULL,
    page_description TEXT NOT NULL,
    page_picture VARCHAR(250),
    page_menu VARCHAR(35),
    PRIMARY KEY (page_data_id)
);