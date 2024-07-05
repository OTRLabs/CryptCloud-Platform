package schema

import (
	"time"

	"entgo.io/ent"
	"entgo.io/ent/schema/field"
)

// User holds the schema definition for the User entity.
type User struct {
	ent.Schema
}

// Fields of the User.
func (User) Fields() []ent.Field {
	return []ent.Field{
		field.String("name").NotEmpty().MaxLen(255),
		field.String("email").NotEmpty().MaxLen(255),
		field.String("password").NotEmpty().MaxLen(255),
		field.Bool("superuser").Default(false),
		field.Bool("active").Default(true),
		field.Time("created_at").Default(time.Now),
		field.Time("updated_at").Default(time.Now),
		field.Time("deleted_at").Nillable().Optional(),
		field.Int("id"),
	}
}

// Edges of the User.
func (User) Edges() []ent.Edge {
	return nil
}
