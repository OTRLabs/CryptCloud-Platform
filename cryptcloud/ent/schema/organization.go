package schema

import "entgo.io/ent"

// Organization holds the schema definition for the Organization entity.
type Organization struct {
	ent.Schema
}

// Fields of the Organization.
func (Organization) Fields() []ent.Field {
	return nil
}

// Edges of the Organization.
func (Organization) Edges() []ent.Edge {
	return nil
}
