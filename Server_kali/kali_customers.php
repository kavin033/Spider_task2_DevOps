<pre>
<?php
include '../load.php';
echo "Server_kali\n";
global $__site_config;
$__site_config = file_get_contents($file."/Server_kali/Customers.json");
function get_config()
{
    global $__site_config;
    $array = json_decode($__site_config, true);
    print_r($array);
}
get_config();
?>
</pre>