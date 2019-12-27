<template>
  <div class="container">
    <div class="row min-vh-100 align-items-center">
      <div class="col-12 text-center">
        <div class="animate">
          <img src="/static/images/batman.png" alt="logo" class="logo">
          <img src="/static/images/back_wheel.png" alt="back wheel" class="wheel back_wheel">
          <img src="/static/images/front_wheel.png" alt="front wheel" class="wheel front_wheel">
        </div>
        <h3 v-bind:style="{ color: color }">
          <slot></slot>
        </h3>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    color: {
      type: String,
      default: 'white'
    }
  },
  data () {
    return {}
  }
}
</script>

<style lang="sass" scoped>
@keyframes flame-animation
  100%
    border-top-width: 1.9em
    border-left-width: .5em
    border-left-width: .5em
@keyframes spin
  0%
    transform: rotate(0deg)
  100%
    transform: rotate(360deg)
.logo
  width: 300px
.wheel
  position: absolute
  bottom: -0.4em
  animation: spin 0.4s linear infinite
.back_wheel
  left: 3.53em
  width: 53px
.front_wheel
  right: 2.53em
  width: 48px
.animate
  display: inline-block
  position: relative
  margin-bottom: 10px
  &:before
    border-left: .65em solid transparent
    border-right: .65em solid transparent
    border-top: 1.75em solid #f7be26
    content: ""
    display: inline-block
    height: .5em
    left: 6%
    position: absolute
    bottom: 0.1em
    transform: rotate(90deg)
    z-index: 6;
    -webkit-animation: flame-animation 0.2s linear infinite
    animation: flame-animation 0.2s linear infinite
</style>
