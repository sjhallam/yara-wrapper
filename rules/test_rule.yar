rule TestRule
{
    strings:
    $my_test_string = "hello world"

    condition:
        $my_test_string
}