<?php
session_start();
include 'conexion.php'; // Incluir la conexión

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $usuario_id = $_SESSION['usuario_id']; // Asegúrate de tener el ID del usuario en la sesión
    $producto_id = $_POST['producto_id'];
    $cantidad = $_POST['cantidad'];
    $precio_unitario = $_POST['precio'];

    // Calcular el total
    $total = $cantidad * $precio_unitario;

    // Insertar pedido
    $query = "INSERT INTO pedidos (usuario_id, total) VALUES (:usuario_id, :total)";
    $stmt = $conexion->prepare($query);
    $stmt->execute(['usuario_id' => $usuario_id, 'total' => $total]);

    // Obtener el ID del pedido recién creado
    $pedido_id = $conexion->lastInsertId();

    // Insertar detalles del pedido
    $query = "INSERT INTO detalles_pedido (pedido_id, producto_id, cantidad, precio_unitario) VALUES (:pedido_id, :producto_id, :cantidad, :precio_unitario)";
    $stmt = $conexion->prepare($query);
    $stmt->execute([
        'pedido_id' => $pedido_id,
        'producto_id' => $producto_id,
        'cantidad' => $cantidad,
        'precio_unitario' => $precio_unitario,
    ]);

    // Redirigir o mostrar un mensaje de éxito
    header("Location: menu.php?success=Pedido realizado con éxito");
    exit();
}
?>
