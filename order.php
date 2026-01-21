<?php
require_once "api.php";

$result = smm_api([
    "action"   => "add",
    "service"  => 1, 
    "link"     => "https://instagram.com/test",
    "quantity" => 100
]);

echo "<pre>";
print_r($result);
echo "</pre>";
