# GraphQl Documentation



GraphQL endpoint can be accessed at:

```
http://localhost
```

## General Queries

The following query will return all news availabe in the local databse.

```
query{
  allNews{
    id
    title
    body
  }
}
```

The following query will return news given id.

```
query{
  newsById(id: "1"){
    id
    title
    body
  }
}
```

The following mutation will add new news.

```
mutation{
  addNews(title: "AI in healthcare", body: "AI in healthcare is the most challlenging ..."){
    news{
      id
      title
      body
    }
  }
}
```
