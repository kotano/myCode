<?php
$request = $_GET['input'];
$response = '';

switch($request)
{
	case 'hello':
	$response = 'hi!';
	break;
	case 'age':
	$response = 'not count :)';
	break;
	case 'name':
	$response = 'Aristofan';
	break;
	case 'time':
	$response = date("H:i:s");
	break;
	case 'date':
	$response = date("Y.m.d");;
	break;
	case 'goodbye':
	$response = 'bye';
	break;
	default:
	$response = 'Moya tvoya ne ponimat';
}
echo $response;
?>
