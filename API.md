# GraphQl Documentation

GraphQL documentation can be accessed from the GraphiQL GUI on `/graphql` endpoint.

```
http://localhost:8080/graphql

```

GraphQL endpoint can be accessed at:

```
http://localhost:8080/
```

## General Queries

The following query will return all news availabe in the local databse.

```
query{
  newss{
    id
    title
    body
  }
}
```

The following query will return news given id.

```
query{
  news(id: "1"){
    id
    title
    body
  }
}
```

The following mutation will add new news.

```
mutation{
  createNews(title: "AI in healthcare", body: "AI in healthcare is the most challlenging ..."){
    news{
      id
      title
      body
    }
  }
}
```
