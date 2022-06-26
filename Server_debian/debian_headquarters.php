<pre>
<?php
include '../load.php';
echo "Server_debian\n";
global $__site_config;
$__site_config = file_get_contents($file."/Server_debian/Headquarters.json");
function get_config()
{
    global $__site_config;
    $array = json_decode($__site_config, true);
    print_r($array);
}
get_config();
?>
</pre>