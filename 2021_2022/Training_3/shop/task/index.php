<!DOCTYPE html>

<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title></title>
    
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Bootstrap core CSS -->
    <link href="./store_files/bootstrap.min.css" rel="stylesheet">
    <!-- Custom styles for this template -->
    <link href="./store_files/shop-homepage.css" rel="stylesheet">
  </head>
  <body>
    <!-- Navigation -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
  <div class="container">
    <a class="navbar-brand" >DonnuCTF Shop</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarResponsive">
      <ul class="navbar-nav ml-auto">
        <li class="nav-item active">
          <a class="nav-link" href="index.php">Home
            <span class="sr-only">(current)</span>
          </a>
        </li>
      </ul>
    </div>
  </div>
</nav>
<!-- Page Content -->
<div class="container">

  <h1 class="my-4">donnuCTF Shop</h1>

  <div class="row">

    <div class="col-lg-9">

      <div id="carouselExampleIndicators" class="carousel slide my-4" data-ride="carousel">
        <ol class="carousel-indicators">
          <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
          <li data-target="#carouselExampleIndicators" data-slide-to="1" class=""></li>
        </ol>
        <div class="carousel-inner" role="listbox">
              <div class="carousel-item active">
                <img class="d-block img-fluid" src="./store_files/silmaril.jpg" alt="First slide">
              </div>
              <div class="carousel-item">
                <img class="d-block img-fluid" src="./store_files/trash.jpg" alt="First slide">
              </div>
        </div>
        <a class="carousel-control-prev" href="" role="button" data-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="" role="button" data-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="sr-only">Next</span>
        </a>
      </div>

     <!-- <div class="row"> -->

           <div class="col-lg-4 col-md-6 mb-4">
             
                <div class="card h-100">
                  <a href="./store_files/silmaril.jpg""><img class="card-img-top" src="./store_files/silmaril.jpg" alt=""></a>
                  <div class="card-body">
                    <h4 class="card-title">
                      <a href="./store_files/silmaril.jpg">Diamond</a>
                    </h4>
                    <h5>999999 ₽</h5>
                    <p class="card-text">Они напоминают кристаллы алмаза,
    но твёрже адаманта, и  нет силы, которая
    могла бы испортить или уничтожить их. </p> 
				<form action="buy.php" method="POST">
                    <input type="hidden" name="id" value="0">
                    <input type="hidden" name="price" value="999999">
                  </div>
                  <div class="card-footer">
                    <button type="submit" class="btn btn-primary" >Купить</button>
                  </div>
                </div>
              </form>
            </div>
            <div class="col-lg-4 col-md-6 mb-4">
              <form action="buy.php" method="POST">
                <div class="card h-100">
                  <a href="./store_files/trash.jpg"><img class="card-img-top" src="./store_files/trash.jpg" alt=""></a>
                  <div class="card-body">
                    <h4 class="card-title">
                      <a href="./store_files/trash.jpg">Trash</a>
                    </h4>
                    <h5>1 ₽</h5>
                    <p class="card-text">Тут мусор валяется, купить не хочешь?</p>
                    <input type="hidden" name="id" value="1">
                    <input type="hidden" name="price" value="1">
                  </div>
                  <div class="card-footer">
                    <button type="submit" class="btn btn-primary" >Купить</button>
                  </div>
                </div>
              </form>
            </div>

      <!-- </div> -->
      <!-- /.row -->

    </div>
    <!-- /.col-lg-9 -->

    <div class="col-lg-3">

      <div class="card my-4">
        <div class="card-header">
          Профиль
        </div>
        <ul class="list-group list-group-flush">
          <li class="list-group-item">Баланс: 100</li>
        </ul>
      </div>

    </div>
    <!-- /.col-lg-3 -->

  </div>
  <!-- /.row -->

</div>
<!-- /.container -->

<!-- Footer -->
<footer class="footer py-5 bg-dark">
  <div class="container">
    <p class="m-0 text-center text-white">Copyright © Store 2021</p>
  </div>
  <!-- /.container -->
</footer>

    <!-- Bootstrap core JavaScript -->
    <script src="./store_files/jquery.min.js"></script>
    <script src="./store_files/bootstrap.bundle.min.js"></script>
  

</body></html>