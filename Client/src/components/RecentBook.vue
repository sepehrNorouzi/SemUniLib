<template>
  <div id="recentBooks">
    <div class="myCard">
      <img
        :src="book.imageUrl"
        alt="alt"
        class="cardImage"
      />
      <div class="cardContent">
        <h3 class="cardTitle">{{book.title}}</h3>
        <p class="cardBody">{{book.author}}</p>
        <p class="cardBody">{{ book.rating }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    props: ['book']
};
</script>

<style scoped>

#recentBooks {
    height: 100%;
}
.cardImage {
  width: 100%;
  transition: all 0.4s;
}

.myCard {
  position: relative;
  max-width: 150px;
  flex: 1;
  border-radius: 7px;
  overflow: hidden;
  transition: all 0.4s;
  height: 100;
}

.cardContent {
  position: absolute;
  bottom: -300px;
  left: 0;
  padding-left: 15px;
  background: linear-gradient(
    to top,
    rgba(0, 0, 0, 1),
    rgba(0, 0, 0, 0.7),
    rgba(0, 0, 0, 0)
  );
  color: white;
  width: 100%;
  transition: all 0.4s;
}

.myCard:hover .cardImage {
  filter: brightness(70%);
}
.myCard:hover .cardContent {
  bottom: 0;
  filter: brightness(100%);
}

.cardTitle {
    font-size: 15px;
}

.cardBody {
    font-size: 10px;
}
</style>
