--
-- Create model Article
--
CREATE TABLE "blog_app_article" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "title" varchar(500) NOT NULL,
    "slug" varchar(250) NOT NULL,
    "body" text NOT NULL,
    "publication_date" datetime NOT NULL,
    "created_date" datetime NOT NULL,
    "updated_date" datetime NOT NULL,
    "status" varchar(10) NOT NULL,
    "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED
);

CREATE INDEX "blog_app_article_author_id_6321872e" ON "blog_app_article" ("author_id");
COMMIT;
