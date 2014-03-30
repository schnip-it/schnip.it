<?

session_start();

include "connect.php";

// Functions

function escape($con, $string) {
	
	return mysqli_real_escape_string($con, $string);
	
}

function getShnipit() {
	
	// To be made later
	
}

function syntaxHighlighter() {
	
	echo "<link type=\"text/css\" rel=\"stylesheet\" href=\"css/syntax/shCore.css\" />";
	echo "<link type=\"text/css\" rel=\"stylesheet\" href=\"css/syntax/shThemeDefault.css\" />";
	
	echo "<script src=\"js/syntax/global/core.js\"></script>";
	echo "<script src=\"js/syntax/javascript.js\"></script>";
	
	echo "<script src=\"js/syntax/javascript.js\"></script>";

	echo "<script src=\"js/syntax/php.js\"></script>";
	
	echo "<script>SyntaxHighlighter.all();</script>";
	
}

include "sql_functions.php";