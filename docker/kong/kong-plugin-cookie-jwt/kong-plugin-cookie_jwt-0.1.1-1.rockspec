package = "kong-plugin-cookie_jwt"

version = "0.1.1-1"

supported_platforms = {"linux"}

source = {
  url = "git://github.com/sebwink/kong-plugin-cookie-jwt",
  tag = "0.1.1-1"
}

description = {
  summary = "A Kong plugin to support cookie-only JWTs.",
  homepage = "http://konghq.com",
  license = "Apache 2.0"
}

dependencies = {
  "lua >= 5.1",
}

build = {
  type = "builtin",
  modules = {
    ["kong.plugins.cookie_jwt.migrations"] = "kong/plugins/cookie_jwt/migrations/init.lua",
    ["kong.plugins.cookie_jwt.migrations.000_base_jwt"] = "kong/plugins/cookie_jwt/migrations/000_base_jwt.lua",
    ["kong.plugins.cookie_jwt.migrations.001_14_to_15"] = "kong/plugins/cookie_jwt/migrations/001_14_to_15.lua",
    ["kong.plugins.cookie_jwt.handler"] = "kong/plugins/cookie_jwt/handler.lua",
    ["kong.plugins.cookie_jwt.schema"] = "kong/plugins/cookie_jwt/schema.lua",
    ["kong.plugins.cookie_jwt.api"] = "kong/plugins/cookie_jwt/api.lua",
    ["kong.plugins.cookie_jwt.daos"] = "kong/plugins/cookie_jwt/daos.lua",
    ["kong.plugins.cookie_jwt.jwt_parser"] = "kong/plugins/cookie_jwt/jwt_parser.lua",
    ["kong.plugins.cookie_jwt.asn_sequence"] = "kong/plugins/cookie_jwt/asn_sequence.lua",
  }
}
