<pre>
<?php
echo "Server_debian\n";
global $__site_config;
$__site_config = file_get_contents("/home/kavin/task2/Server_debian/Customers.json");
function get_config()
{
    global $__site_config;
    $array = json_decode($__site_config, true);
    print_r($array);
}
get_config();
?>
</pre>