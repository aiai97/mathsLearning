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

import org.springframework.transaction.TransactionStatus;
import org.springframework.transaction.support.TransactionCallback;
import org.springframework.transaction.support.TransactionTemplate;

public class OrderService {
    private TransactionTemplate transactionTemplate;
    private InventoryService inventoryService;
    private OrderService orderService;
    private PaymentService paymentService;

    public OrderService(TransactionTemplate transactionTemplate, InventoryService inventoryService,
            OrderService orderService, PaymentService paymentService) {
        this.transactionTemplate = transactionTemplate;
        this.inventoryService = inventoryService;
        this.orderService = orderService;
        this.paymentService = paymentService;
    }

    public void placeOrder(final Order order) {
        transactionTemplate.execute(new TransactionCallback<Void>() {
            @Override
            public Void doInTransaction(TransactionStatus status) {
                try {
                    // 扣减库存
                    inventoryService.reduceStock(order.getProduct(), order.getQuantity());

                    // 生成订单
                    orderService.createOrder(order);

                    // 扣款
                    paymentService.processPayment(order);

                    return null;
                } catch (Exception e) {
                    status.setRollbackOnly(); // 手动触发事务回滚
                    throw e;
                }
            }
        });
    }
}
import org.springframework.transaction.TransactionStatus;
import org.springframework.transaction.support.TransactionCallback;
import org.springframework.transaction.support.TransactionTemplate;

public class RatingService {
    private TransactionTemplate transactionTemplate;
    private RiskAssessmentService riskAssessmentService;
    private CreditRatingService creditRatingService;

    public RatingService(TransactionTemplate transactionTemplate, RiskAssessmentService riskAssessmentService,
            CreditRatingService creditRatingService) {
        this.transactionTemplate = transactionTemplate;
        this.riskAssessmentService = riskAssessmentService;
        this.creditRatingService = creditRatingService;
    }

    public RatingResult calculateRating(final Client client) {
        return transactionTemplate.execute(new TransactionCallback<RatingResult>() {
            @Override
            public RatingResult doInTransaction(TransactionStatus status) {
                try {
                    // 进行风险评估
                    RiskAssessmentResult riskAssessmentResult = riskAssessmentService.assessRisk(client);

                    // 进行信用评级
                    CreditRatingResult creditRatingResult = creditRatingService.rateCredit(client, riskAssessmentResult);

                    // 返回评级结果
                    return new RatingResult(client, riskAssessmentResult, creditRatingResult);
                } catch (Exception e) {
                    status.setRollbackOnly(); // 手动触发事务回滚
                    throw e;
                }
            }
        });
    }
}
@Transactional 注解和 TransactionTemplate 都是用于在 Spring 中进行事务管理的方式，它们的主要区别在于使用方式和适用场景。

使用方式：

@Transactional 注解是一种声明式事务管理的方式。你可以将它直接应用于方法或类级别，并通过在方法或类上添加注解来启用事务管理。Spring 会在运行时通过 AOP（面向切面编程）来拦截带有 @Transactional 注解的方法，并自动管理事务的开始、提交和回滚。
TransactionTemplate 是一种编程式事务管理的方式。你可以在代码中显式地使用 TransactionTemplate 来控制事务的开始、提交和回滚。通过调用 transactionTemplate.execute() 方法，你可以将事务相关的逻辑包装在一个回调对象中，以确保在事务内执行。
适用场景：

@Transactional 注解适用于方法级别的事务管理，尤其适用于简单的事务场景。它提供了一种声明式的方式来管理事务，使得代码更加简洁和可读。使用注解方式时，事务的管理和配置是通过注解参数来控制的，例如事务的传播行为、隔离级别、超时设置等。
TransactionTemplate 适用于更复杂的事务场景，特别是需要在事务中执行一系列操作或需要在事务内进行条件判断和异常处理的情况。通过使用 TransactionTemplate，你可以以编程方式控制事务的开始、提交和回滚，灵活处理异常情况，并实现更精细的事务控制逻辑。
在实际应用中，选择使用 @Transactional 注解还是 TransactionTemplate 取决于项目的需求和开发团队的偏好。对于简单的事务场景，使用 @Transactional 注解能够提供更简洁的代码，并充分利用 Spring 的声明式事务管理功能。而对于复杂的事务场景，使用 TransactionTemplate 可以提供更多的灵活性和控制权。

需要注意的是，无论使用哪种方式，都需要确保正确配置事务管理器和数据源，并将它们与 Spring Boot 应用程序的主配置类关联起来，以便启用和管理事务
