# NOTE: Generated By HttpRunner v3.1.6
# FROM: 2021-8-22.har


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseT2021822(HttpRunner):
    config = (
        Config("首页接口")
            .variables(
            **{
                "foo1": "testsuite_config_bar1",
                "expect_foo1": "testsuite_config_bar1",
                "expect_foo2": "config_bar2",
            }
        )
            .base_url("http://testapi.qingpinyouxuan.com")
            .verify(False)
    )

    teststeps = [
        Step(
            RunRequest("/app/user/userInfo")
            .get("/app/user/userInfo")
            .with_headers(
                **{
                    "token": "AUTH_USER_96_c4ce610235a44f249c0b18a9ff5fc9c0",
                    "phone": "19821244219",
                    "channel": "qingpin",
                    "system": "android",
                    "appversion": "1.3.2",
                    "phoneversion": "11",
                    "brand": "Xiaomi",
                    "uuid": "00000000-007e-0d16-ffff-ffffef05ac4a",
                    "deviceType": "OAID",
                    "deviceValue": "577f8394434bd97efa61e4e0576140df",
                    "phonemodel": "Mi9 Pro 5G",
                    "Host": "testapi.qingpinyouxuan.com",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip",
                    "User-Agent": "okhttp/3.10.0",
                    "If-Modified-Since": "Wed, 22 Sep 2021 06:10:17 GMT",
                }
            )
            .extract().with_jmespath()
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.code", "10000")
            .assert_equal("body.msg", "操作成功！")
        ),
        Step(
            RunRequest("/app/user/info")
            .put("/app/user/info")
            .with_headers(
                **{
                    "token": "AUTH_USER_96_c4ce610235a44f249c0b18a9ff5fc9c0",
                    "phone": "19821244219",
                    "channel": "qingpin",
                    "system": "android",
                    "appversion": "1.3.2",
                    "phoneversion": "11",
                    "brand": "Xiaomi",
                    "uuid": "00000000-007e-0d16-ffff-ffffef05ac4a",
                    "deviceType": "OAID",
                    "deviceValue": "577f8394434bd97efa61e4e0576140df",
                    "phonemodel": "Mi9 Pro 5G",
                    "Content-Type": "application/json;charset=UTF-8",
                    "Content-Length": "70",
                    "Host": "testapi.qingpinyouxuan.com",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip",
                    "User-Agent": "okhttp/3.10.0",
                }
            )
            .with_json(
                {
                    "deviceToken": "Agb3XAYbzlBKZ4c5SSXpS1mgL8_ngDSw46sOzEUmd6y9",
                    "sex": 0,
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.data", None)
            .assert_equal("body.code", "10000")
            .assert_equal("body.msg", "操作成功！")
        ),
        Step(
            RunRequest("/goods/category/list")
            .get("/goods/category/list")
            .with_params(**{"type": "1"})
            .with_headers(
                **{
                    "token": "AUTH_USER_96_c4ce610235a44f249c0b18a9ff5fc9c0",
                    "phone": "19821244219",
                    "channel": "qingpin",
                    "system": "android",
                    "appversion": "1.3.2",
                    "phoneversion": "11",
                    "brand": "Xiaomi",
                    "uuid": "00000000-007e-0d16-ffff-ffffef05ac4a",
                    "deviceType": "OAID",
                    "deviceValue": "577f8394434bd97efa61e4e0576140df",
                    "phonemodel": "Mi9 Pro 5G",
                    "Host": "testapi.qingpinyouxuan.com",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip",
                    "User-Agent": "okhttp/3.10.0",
                    "If-Modified-Since": "Wed, 22 Sep 2021 06:10:17 GMT",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.code", "10000")
            .assert_equal("body.msg", "操作成功！")
        ),
        Step(
            RunRequest("/goldcoin/signed/1")
            .get("/goldcoin/signed/1")
            .with_headers(
                **{
                    "token": "AUTH_USER_96_c4ce610235a44f249c0b18a9ff5fc9c0",
                    "phone": "19821244219",
                    "channel": "qingpin",
                    "system": "android",
                    "appversion": "1.3.2",
                    "phoneversion": "11",
                    "brand": "Xiaomi",
                    "uuid": "00000000-007e-0d16-ffff-ffffef05ac4a",
                    "deviceType": "OAID",
                    "deviceValue": "577f8394434bd97efa61e4e0576140df",
                    "phonemodel": "Mi9 Pro 5G",
                    "Host": "testapi.qingpinyouxuan.com",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip",
                    "User-Agent": "okhttp/3.10.0",
                    "If-Modified-Since": "Wed, 22 Sep 2021 06:10:17 GMT",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.data", None)
            .assert_equal("body.code", "10028")
            .assert_equal("body.msg", "金币签到异常")
        ),
        Step(
            RunRequest("/app/api/banner/location/1")
            .get("/app/api/banner/location/1")
            .with_headers(
                **{
                    "token": "AUTH_USER_96_c4ce610235a44f249c0b18a9ff5fc9c0",
                    "phone": "19821244219",
                    "channel": "qingpin",
                    "system": "android",
                    "appversion": "1.3.2",
                    "phoneversion": "11",
                    "brand": "Xiaomi",
                    "uuid": "00000000-007e-0d16-ffff-ffffef05ac4a",
                    "deviceType": "OAID",
                    "deviceValue": "577f8394434bd97efa61e4e0576140df",
                    "phonemodel": "Mi9 Pro 5G",
                    "Host": "testapi.qingpinyouxuan.com",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip",
                    "User-Agent": "okhttp/3.10.0",
                    "If-Modified-Since": "Wed, 22 Sep 2021 06:10:17 GMT",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.code", "10000")
            .assert_equal("body.msg", "操作成功！")
        ),
        Step(
            RunRequest("/index/getBannerList")
            .get("/index/getBannerList")
            .with_headers(
                **{
                    "token": "AUTH_USER_96_c4ce610235a44f249c0b18a9ff5fc9c0",
                    "phone": "19821244219",
                    "channel": "qingpin",
                    "system": "android",
                    "appversion": "1.3.2",
                    "phoneversion": "11",
                    "brand": "Xiaomi",
                    "uuid": "00000000-007e-0d16-ffff-ffffef05ac4a",
                    "deviceType": "OAID",
                    "deviceValue": "577f8394434bd97efa61e4e0576140df",
                    "phonemodel": "Mi9 Pro 5G",
                    "Host": "testapi.qingpinyouxuan.com",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip",
                    "User-Agent": "okhttp/3.10.0",
                    "If-Modified-Since": "Wed, 22 Sep 2021 06:10:17 GMT",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.code", "10000")
            .assert_equal("body.msg", "操作成功！")
        ),
    ]


if __name__ == "__main__":
    TestCaseT2021822().test_start()
