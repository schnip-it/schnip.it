<?

$mysqli = new mysqli('localhost', 'shnip_dbuser', 'HmgoA9D4rqFs', 'shnip_content');

/*
 * This is the "official" OO way to do it,
 * BUT $connect_error was broken until PHP 5.2.9 and 5.3.0.
 */
if ($mysqli->connect_error) {
    die('Connect Error (' . $mysqli->connect_errno . ') '
            . $mysqli->connect_error);
}

$con = mysqli_connect('localhost', 'shnip_dbuser', 'HmgoA9D4rqFs', 'shnip_content') or die("Mysql error");