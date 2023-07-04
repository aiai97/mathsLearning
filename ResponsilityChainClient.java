package com.alibaba.cloud.examples;

// 权限认证请求类
class AuthenticationRequest {
    private String username;
    private String password;

    public AuthenticationRequest(String username, String password) {
        this.username = username;
        this.password = password;
    }

    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }
}

// 权限认证处理者抽象类
abstract class AuthenticationHandler {
    private AuthenticationHandler nextHandler;

    public void setNextHandler(AuthenticationHandler nextHandler) {
        this.nextHandler = nextHandler;
    }

    public void handleRequest(AuthenticationRequest request) {
        if (canHandle(request)) {
            processRequest(request);
        } else if (nextHandler != null) {
            nextHandler.handleRequest(request);
        } else {
            System.out.println("Authentication failed.");
        }
    }

    protected abstract boolean canHandle(AuthenticationRequest request);

    protected abstract void processRequest(AuthenticationRequest request);
}

// 用户名密码验证处理者
class UsernamePasswordHandler extends AuthenticationHandler {
    @Override
    protected boolean canHandle(AuthenticationRequest request) {
        // 判断是否可以处理用户名密码验证
        // 根据请求的内容进行判断
        // 返回true表示可以处理，false表示不能处理
        return request.getUsername() != null && request.getPassword() != null;
    }

    @Override
    protected void processRequest(AuthenticationRequest request) {
        // 处理用户名密码验证
        // 实现具体的验证逻辑
        System.out.println("Username password authentication successful.");
    }
}

// 角色验证处理者
class RoleHandler extends AuthenticationHandler {
    @Override
    protected boolean canHandle(AuthenticationRequest request) {
        // 判断是否可以处理角色验证
        // 根据请求的内容进行判断
        // 返回true表示可以处理，false表示不能处理
        return request.getUsername() != null && request.getUsername().equals("admin");
    }

    @Override
    protected void processRequest(AuthenticationRequest request) {
        // 处理角色验证
        // 实现具体的验证逻辑
        System.out.println("Role authentication successful.");
    }
}

// 资源权限验证处理者
class ResourceHandler extends AuthenticationHandler {
    @Override
    protected boolean canHandle(AuthenticationRequest request) {
        // 判断是否可以处理资源权限验证
        // 根据请求的内容进行判断
        // 返回true表示可以处理，false表示不能处理
        return request.getUsername() != null && request.getUsername().equals("admin")
                && request.getPassword() != null && request.getPassword().equals("password");
    }

    @Override
    protected void processRequest(AuthenticationRequest request) {
        // 处理资源权限验证
        // 实现具体的验证逻辑
        System.out.println("Resource authentication successful.");
    }
}

// 客户端使用示例
class ResponsilityChainClient {
    public static void main(String[] args) {
        // 创建权限认证处理者
        AuthenticationHandler usernamePasswordHandler = new UsernamePasswordHandler();
        AuthenticationHandler roleHandler = new RoleHandler();
        AuthenticationHandler resourceHandler = new ResourceHandler();

        // 构建责任链
        usernamePasswordHandler.setNextHandler(roleHandler);
        roleHandler.setNextHandler(resourceHandler);

        // 创建认证请求
        AuthenticationRequest request = new AuthenticationRequest("admin", "password");

        // 处理认证请求
        usernamePasswordHandler.handleRequest(request);
    }
}
