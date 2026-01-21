<?php
require_once "api.php";

$result = smm_api([
    "action" => "services"
]);

echo "<pre>";
print_r($result);
echo "</pre>";
