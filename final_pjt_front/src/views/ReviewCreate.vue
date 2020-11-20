<template>

<div class='container'>
<form>
  <div class="form-group">
    <label for="title"> 글 제목 </label>
    <input type="email" class="form-control" id="title" placeholder="글 제목">
  </div>

  <div class="form-group">
    <label for="content">Content</label>
    <textarea class="form-control" id="content" rows="3"></textarea>
  </div>

  <div class="form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">사용자 약관에 동의합니다.</label>
  </div>
  <button type="submit" class="btn btn-primary">제출</button>
  <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone elsedd.</small>
</form>
</div>
  
</template>

<script>
export default {

}
</script>

<style>

</style>