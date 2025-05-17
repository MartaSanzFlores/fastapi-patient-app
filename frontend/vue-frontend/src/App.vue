<script setup>
  import { ref } from 'vue'
  import PatientsList from './components/PatientList.vue'
  import PatientForm from './components/PatientForm.vue'

  const patientForm = ref(false)

  function formModal() {
    patientForm.value = true
  } 

</script>

<template>
  <main>
    <div v-if="!patientForm">
      <button @click="formModal">New patient</button>
      <PatientsList />
    </div>
    <PatientForm v-if="patientForm" @submitted="patientForm = false" />
  </main>
</template>