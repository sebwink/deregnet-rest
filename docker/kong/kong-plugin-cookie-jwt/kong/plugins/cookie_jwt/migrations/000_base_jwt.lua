return {
  postgres = {
    up = [[
      CREATE TABLE IF NOT EXISTS "cookie_jwt_secrets" (
        "id"              UUID                         PRIMARY KEY,
        "created_at"      TIMESTAMP WITHOUT TIME ZONE  DEFAULT (CURRENT_TIMESTAMP(0) AT TIME ZONE 'UTC'),
        "consumer_id"     UUID                         REFERENCES "consumers" ("id") ON DELETE CASCADE,
        "key"             TEXT                         UNIQUE,
        "secret"          TEXT,
        "algorithm"       TEXT,
        "rsa_public_key"  TEXT
      );

      CREATE INDEX IF NOT EXISTS "cookie_jwt_secrets_consumer_id" ON "cookie_jwt_secrets" ("consumer_id");
      CREATE INDEX IF NOT EXISTS "cookie_jwt_secrets_secret"      ON "cookie_jwt_secrets" ("secret");
    ]],
  },

  cassandra = {
    up = [[
      CREATE TABLE IF NOT EXISTS cookie_jwt_secrets(
        id             uuid PRIMARY KEY,
        created_at     timestamp,
        consumer_id    uuid,
        algorithm      text,
        rsa_public_key text,
        key            text,
        secret         text
      );
      CREATE INDEX IF NOT EXISTS ON cookie_jwt_secrets(key);
      CREATE INDEX IF NOT EXISTS ON cookie_jwt_secrets(secret);
      CREATE INDEX IF NOT EXISTS ON cookie_jwt_secrets(consumer_id);
    ]],
  },
}
