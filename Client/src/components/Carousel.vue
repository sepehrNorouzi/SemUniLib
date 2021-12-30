<template>
  <div
    id="carouselExampleIndicators"
    class="carousel slide"
    data-bs-ride="carousel"
  >
    <div class="carousel-indicators">
      <button
        type="button"
        data-bs-target="#carouselExampleIndicators"
        data-bs-slide-to="0"
        class="active"
        aria-current="true"
        aria-label="Slide 1"
      ></button>
      <button
        type="button"
        data-bs-target="#carouselExampleIndicators"
        data-bs-slide-to="1"
        aria-label="Slide 2"
      ></button>
      <button
        type="button"
        data-bs-target="#carouselExampleIndicators"
        data-bs-slide-to="2"
        aria-label="Slide 3"
      ></button>
    </div>
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img :src="books[0].imageUrl" class="d-block  carImg" alt="BOOK" />
      </div>
      <div class="carousel-item">
        <img :src="books[1].imageUrl" class="d-block  carImg" alt="BOOK" />
      </div>
      <div class="carousel-item">
        <img :src="books[2].imageUrl" class="d-block  carImg" alt="BOOK" />
      </div>
    </div>
    <button
      class="carousel-control-prev"
      type="button"
      data-bs-target="#carouselExampleIndicators"
      data-bs-slide="prev"
    >
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button
      class="carousel-control-next"
      type="button"
      data-bs-target="#carouselExampleIndicators"
      data-bs-slide="next"
    >
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
</template>

<script>
export default {

    props: ['books']
};
</script>

<style>

.carousel-inner {
    height: 100%;
}

.carousel-item {
    height: 100%;
    position: relative;
}

.carousel {
    height: 30rem;
}

.carImg {
    height: 100%;
    position: absolute;
    top:50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
</style>
