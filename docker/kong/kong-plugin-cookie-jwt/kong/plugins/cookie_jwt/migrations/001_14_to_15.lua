return {
  postgres = {
    up = [[
      ALTER TABLE IF EXISTS ONLY "cookie_jwt_secrets"
        ALTER "created_at" TYPE TIMESTAMP WITH TIME ZONE USING "created_at" AT TIME ZONE 'UTC',
        ALTER "created_at" SET DEFAULT CURRENT_TIMESTAMP(0) AT TIME ZONE 'UTC';

      DO $$
      BEGIN
        ALTER INDEX IF EXISTS "cookie_jwt_secrets_consumer_id" RENAME TO "cookie_jwt_secrets_consumer_id_idx";
      EXCEPTION WHEN DUPLICATE_TABLE THEN
        -- Do nothing, accept existing state
      END;
      $$;

      DO $$
      BEGIN
        ALTER INDEX IF EXISTS "cookie_jwt_secrets_secret" RENAME TO "cookie_jwt_secrets_secret_idx";
      EXCEPTION WHEN DUPLICATE_TABLE THEN
        -- Do nothing, accept existing state
      END;
      $$;

      -- Unique constraint on "key" already adds btree index
      DROP INDEX IF EXISTS "cookie_jwt_secrets_key";
    ]],
  },

  cassandra = {
    up = [[
    ]],
  },
}
