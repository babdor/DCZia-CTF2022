<html>
<head>
<title>My Simple Image Viewer</title>
</head>
<body>

<p>
    Which file do you want to view? Select it from the dropdown and then
click the button!
</p>

<form>
<select name="file" id="file">
<option value="buffalo.php">Buffalo!</option>
<option value="graphicdesign.php">Graphic Design is my Passion</option>
<option value="greatvideo.php">A Great Video</option>
</select>
<input type="submit" />
</form>


<p>
    Your file:
</p>
<?php
   if(array_key_exists("file", $_GET))
   {
       echo file_get_contents($_GET["file"]);
   }
   else
   {
       echo file_get_contents("index-default.php");
   }
?>

<!--
    TODO: how the heck do people keep getting the flag file out of here?
They can't go to it directly... if you go to flag.php directly there's no
output
  -->

</body>
</html>
