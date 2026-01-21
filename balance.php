<?php
require_once "api.php";

$result = smm_api([
    "action" => "balance"
]);

echo "<pre>";
print_r($result);
echo "</pre>";
