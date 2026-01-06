# Architecture Overview

Corrigi o erro de renderização: o problema vinha do rótulo da seta contendo parênteses `HTTP(S)` — o parser do Mermaid pode interpretar parênteses especiais dentro de rótulos se não estiverem entre aspas. A correção foi envolver o texto do rótulo entre aspas: `"HTTP(S) requests"`. Em geral, sempre que um label de seta contiver parênteses, barras ou caracteres especiais, coloque-o entre aspas.

Abaixo está o diagrama Mermaid corrigido.

```mermaid
flowchart LR
  %% Clients / Edge
  subgraph Clients["Clients"]
    direction TB
    User["User (Web / Mobile)"]
  end

  subgraph Edge["Edge / Network"]
    direction TB
    CDN["CDN"]
    WAF["WAF / Edge Security"]
  end

  User -->|"HTTP(S) requests"| CDN --> WAF --> APIGW["API Gateway / Ingress"]

  %% Platform / Cluster
  subgraph Platform["Platform (Kubernetes Cluster)"]
    direction LR
    LB["Load Balancer"]
    Cache["Cache (Redis)"]
    Broker["Message Broker (Kafka / RabbitMQ)"]

    subgraph Services["Microservices"]
      direction TB
      Auth["Auth Service (OAuth / JWT)"]
      UserSvc["User Service"]
      ProductSvc["Product / Catalog Service"]
      OrderSvc["Order Service"]
      InventorySvc["Inventory Service"]
      Notifications["Notifications Service"]
    end

    subgraph Data["Datastores"]
      direction TB
      UserDB["Users DB (SQL)"]
      CatalogDB["Catalog DB (SQL)"]
      OrdersDB["Orders DB (SQL)"]
      InventoryDB["Inventory DB (NoSQL)"]
    end
  end

  APIGW -->|routes| LB
  LB --> UserSvc
  LB --> ProductSvc
  LB --> OrderSvc
  LB --> InventorySvc
  LB --> Auth

  APIGW --> Cache
  OrderSvc -->|publish event| Broker
  Broker --> InventorySvc

  UserSvc --> UserDB
  ProductSvc --> CatalogDB
  OrderSvc --> OrdersDB
  InventorySvc --> InventoryDB

  %% External Integrations
  Payment["Payment Provider (External)"]
  Email["Email / SMS Provider (External)"]
  OrderSvc -->|payment API| Payment
  Notifications -->|send email/sms| Email
  OrderSvc --> Notifications

  %% Observability & CI/CD
  Monitoring["Monitoring & Logging (Prometheus / ELK / Grafana)"]
  Tracing["Tracing (Jaeger / OpenTelemetry)"]
  CI["CI/CD Pipeline"]

  Auth --> Monitoring
  UserSvc --> Monitoring
  ProductSvc --> Monitoring
  OrderSvc --> Monitoring
  InventorySvc --> Monitoring
  Broker --> Monitoring

  Auth --> Tracing
  UserSvc --> Tracing
  ProductSvc --> Tracing
  OrderSvc --> Tracing
  InventorySvc --> Tracing

  CI -->|deploy| Platform
```

O que corrigi
- Coloquei o label da seta com parênteses entre aspas: `"HTTP(S) requests"`.

Boas práticas para evitar erros similares
- Ponha labels de setas entre aspas sempre que tiverem parênteses, barras, dois-pontos ou outros caracteres especiais.
- Teste o diagrama em https://mermaid.live/ ou no preview do GitHub para validar.
- Se aparecer outro erro, copie a mensagem e eu ajusto o diagrama.

Quer que eu gere uma versão com rótulos em português ou exporte o diagrama para SVG/PNG?
