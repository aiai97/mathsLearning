Conflicts
You can avoid them, by employing a pessimistic locking mechanism (e.g. Read/Write locks, Two-Phase Locking)
You can allow conflicts to occur, but you need to detect them using an optimistic locking mechanism (e.g. logical clock, MVCC)

Serializable, Repeatable reads, Read committed, Read uncommitted
top-down is the order of execution.

In the process of introducing MVCC we can easily capture the following key points:

Multiple versions.
Garbage handling.
Improving the efficiency of concurrent operations.
https://www.cncf.io/blog/2023/05/16/database-isolation-levels-and-mvcc/
While the above example looks specifically at the differences between the Snapshot isolation level and Serializable, we have not yet fully described the characteristics of Snapshot:

Transactions in Snapshot have two important timestamps, a read timestamp R and a write timestamp W. All read operations after R can only read the data committed before R.
Snapshot allows two transactions that do not have a write intersection to execute simultaneously and in parallel.
In the process of introducing MVCC we can easily capture the following key points:

Multiple versions.
Garbage handling.
Improving the efficiency of concurrent operations.

If Transaction 1 in Table 3 has two consecutive read operations while the user wants to guarantee that the same value is read, then the repeatable read isolation level should be used.

在Spring Boot的主配置类上添加@EnableTransactionManagement注解，以启用Spring的事务管理功能。

在数据库配置中，配置数据源（DataSource）的相关信息，例如数据库连接URL、用户名和密码等。

创建一个事务管理器的Bean，并将数据源配置为其属性。可以使用Spring Boot提供的默认事务管理器，如DataSourceTransactionManager。

在需要进行事务管理的方法上添加@Transactional注解。该注解可以添加在类级别或方法级别，用于标识需要进行事务控制的方法。

